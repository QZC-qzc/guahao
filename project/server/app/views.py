import json
import time
import uuid

from django.core.cache import cache
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.views import View

from app import models


'''
基础处理类，其他处理继承这个类
'''
class BaseView(View):
    '''
    检查指定的参数是否存在
    存在返回 True
    不存在返回 False
    '''
    def isExit(param):

        if (param == None) or (param == ''):
            return False
        else:
            return True

    '''
    转换分页查询信息
    '''
    def parasePage(pageIndex, pageSize, pageTotal, count, data):

        return {'pageIndex': pageIndex, 'pageSize': pageSize, 'pageTotal': pageTotal, 'count': count, 'data': data}

    '''
    转换分页查询信息
    '''
    def parasePage(pageIndex, pageSize, pageTotal, count, data):
        return {'pageIndex': pageIndex, 'pageSize': pageSize, 'pageTotal': pageTotal, 'count': count, 'data': data}

    '''
    成功响应信息
    '''
    def success(msg='处理成功'):
        resl = {'code': 0, 'msg': msg}
        return HttpResponse(json.dumps(resl), content_type='application/json; charset=utf-8')

    '''
    成功响应信息, 携带数据
    '''
    def successData(data, msg='处理成功'):
        resl = {'code': 0, 'msg': msg, 'data': data}
        return HttpResponse(json.dumps(resl), content_type='application/json; charset=utf-8')

    '''
    系统警告信息
    '''
    def warn(msg='操作异常，请重试'):
        resl = {'code': 1, 'msg': msg}
        return HttpResponse(json.dumps(resl), content_type='application/json; charset=utf-8')

    '''
    系统异常信息
    '''
    def error(msg='系统异常'):
        resl = {'code': 2, 'msg': msg}
        return HttpResponse(json.dumps(resl), content_type='application/json; charset=utf-8')

'''
系统处理
'''
class SysView(BaseView):

    def get(self, request, module, *args, **kwargs):

        if module == 'info':
            return SysView.getSessionInfo(request)
        elif module == 'checkPwd':
            return SysView.checkPwd(request)
        elif module == 'exit':
            return SysView.exit(request)
        elif module == 'statis':
            return SysView.getStatis(request)
        else:
            return BaseView.error()

    def post(self, request, module, *args, **kwargs):

        if module == 'info':
            return SysView.updSessionInfo(request)
        elif module == 'pwd':
            return SysView.updSessionPwd(request)
        elif module == 'login':
           return SysView.login(request)
        else:
            return BaseView.error()

    '''
    获取系统统计信息
    '''
    def getStatis(request):

        resl = {
            'officeTotal': models.Offices.objects.all().count(),
            'doctorTotal': models.Doctors.objects.all().count()
        }

        return BaseView.successData(resl)


    '''
    用户登陆处理
    '''
    def login(request):

        userName = request.POST.get('userName')
        passWord = request.POST.get('passWord')
        flag = int(request.POST.get('flag'))

        user = models.Users.objects.filter(userName=userName)

        if (user.exists()):

            user = user.first()

            if (flag == 0) & (user.type == 2) :

                return SysView.warn('普通用户无权使用管理功能')

            elif (flag == 1) & (user.type != 2):
                return SysView.warn('管理员或医师无法登陆')

            else:
                if user.passWord == passWord:

                    token = uuid.uuid4()

                    resl = {
                        'token': str(token)
                    }

                    cache.set(token, user.id, 60*60*60*3)

                    return SysView.successData(resl)
                else:
                    return SysView.error('用户密码输入错误')
        else:
            return SysView.error('用户名输入错误')

    # 获取登陆用户信息
    def getLoginUser(token):

        user = models.Users.objects.filter(id=cache.get(token)).first()

        if user.type == 2:

            patient = models.Patients.objects.filter(user__id=user.id).first()

            resl = {
                'id': user.id,
                'userName': user.userName,
                'passWord': user.passWord,
                'name': user.name,
                'age': user.age,
                'gender': user.gender,
                'phone': user.phone,
                'createTime': user.createTime,
                'type': user.type,
                'card': patient.card,
                'address': patient.address,
            }

            return resl
        else:
            resl = {
                'id': user.id,
                'userName': user.userName,
                'passWord': user.passWord,
                'name': user.name,
                'age': user.age,
                'gender': user.gender,
                'phone': user.phone,
                'createTime': user.createTime,
                'type': user.type,
            }

            return resl



    '''
    用户登出处理
    '''
    def exit(request):

        token = request.GET.get('token')

        cache.delete(token)

        return BaseView.success()

    '''
    密码校验
    '''
    def checkPwd(request):

        oldPwd = request.GET.get('oldPwd')

        loginUser = SysView.getLoginUser(request.GET.get('token'))

        if(loginUser['passWord'] == oldPwd):
            return BaseView.success()
        else:
            return BaseView.warn('原始密码输入错误')

    '''
    获取登陆用户信息
    '''
    def getSessionInfo(request):

        loginUser = SysView.getLoginUser(request.GET.get('token'))

        return BaseView.successData(loginUser)

    '''
    修改登陆用户信息
    '''
    def updSessionInfo(request):

        loginUser = SysView.getLoginUser(request.POST.get('token'))

        if (request.POST.get('userName') != loginUser['userName']) & \
            (models.Users.objects.filter(userName=request.POST.get('userName')).exists()):

            return BaseView.warn('用户账号已存在无法重复添加')

        if loginUser['type'] == 2:

            models.Patients.objects. \
                filter(user__id=loginUser['id']).update(
                address=request.POST.get('address'),
                card=request.POST.get('card')
            )

        models.Users.objects. \
            filter(id=loginUser['id']).update(
            userName=request.POST.get('userName'),
            name=request.POST.get('name'),
            gender=request.POST.get('gender'),
            age=request.POST.get('age'),
        )

        return BaseView.success()

    '''
    修改登陆用户密码
    '''
    def updSessionPwd(request):

        loginUser = SysView.getLoginUser(request.POST.get('token'))

        models.Users.objects. \
            filter(id=loginUser['id']).update(
            passWord=request.POST.get('newPwd'),
        )

        return BaseView.success()

'''
通知信息处理
'''
class NoticesView(BaseView):

    def get(self, request, module, *args, **kwargs):

        if module == 'info':
            return NoticesView.getInfo(request)
        elif module == 'top':
            return NoticesView.getTopList(request)
        elif module == 'page':
            return NoticesView.getPageInfo(request)
        else:
            return BaseView.error()

    def post(self, request, module, *args, **kwargs):

        if module == 'add':
            return NoticesView.addInfo(request)
        elif module == 'del':
            return NoticesView.delInfo(request)
        else:
            return BaseView.error()

    '''
    获取指定数据
    '''
    def getInfo(request):

        data = models.Notices.objects.filter(id=request.GET.get('id')).first()

        resl = {
            'id': data.id,
            'title': data.title,
            'detail': data.detail,
            'putTime': data.putTime,
        }

        return BaseView.successData(resl)

    '''
    获取通知记录前七条
    '''
    def getTopList(request):

        resl = []

        noticeses = models.Notices.objects.all().order_by("-putTime")[:7];

        for item in list(noticeses):
            temp = {
                'id': item.id,
                'title': item.title,
                'detail': item.detail,
                'putTime': item.putTime,
            }
            resl.append(temp)

        return BaseView.successData(resl)


    '''
    分页获取数据
    '''
    def getPageInfo(request):

        pageIndex = request.GET.get('pageIndex', 1)
        pageSize = request.GET.get('pageSize', 10)
        title = request.GET.get('title')

        qruery = Q();

        if BaseView.isExit(title):
            qruery = qruery & Q(title__contains=title)

        data = models.Notices.objects.filter(qruery).order_by("-putTime")

        paginator = Paginator(data, pageSize)

        resl = []

        for item in list(paginator.page(pageIndex)):
            temp = {
                'id': item.id,
                'title': item.title,
                'detail': item.detail,
                'putTime': item.putTime,
            }
            resl.append(temp)

        temp = BaseView.parasePage(int(pageIndex), int(pageSize),
                                   paginator.page(pageIndex).paginator.num_pages,
                                   paginator.count, resl)

        return BaseView.successData(temp)

    '''
    添加数据
    '''
    def addInfo(request):

        models.Notices.objects.create(
                                        title=request.POST.get('title'),
                                        detail=request.POST.get('detail'),
                                        putTime=time.strftime("%Y-%m-%d", time.localtime())
                                    )

        return BaseView.success()

    '''
    删除数据
    '''
    def delInfo(request):

        models.Notices.objects.filter(id=request.POST.get('id')).delete()

        return BaseView.success()

'''
科室信息管理
'''
class OfficesView(BaseView):

    def get(self, request, module, *args, **kwargs):

        if module == 'info':
            return OfficesView.getInfo(request)
        elif module == 'all':
            return OfficesView.getAll(request)
        elif module == 'page':
            return OfficesView.getPageInfo(request)
        else:
            return BaseView.error()

    def post(self, request, module, *args, **kwargs):

        if module == 'add':
            return OfficesView.addInfo(request)
        elif module == 'upd':
            return OfficesView.updInfo(request)
        elif module == 'del':
            return OfficesView.delInfo(request)
        else:
            return BaseView.error()

    '''
    获取指定数据
    '''
    def getInfo(request):

        data = models.Offices.objects.filter(id=request.GET.get('id')).first()

        resl = {
            'id': data.id,
            'name': data.name,
            'detail': data.detail,
            'putTime': data.putTime,
        }

        return BaseView.successData(resl)

    '''
    获取全部
    '''
    def getAll(request):

        data = models.Offices.objects.all()

        resl = []

        for item in list(data):
            temp = {
                'id': item.id,
                'name': item.name,
                'detail': item.detail,
                'putTime': item.putTime,
            }
            resl.append(temp)

        return BaseView.successData(resl)


    '''
    分页获取数据
    '''
    def getPageInfo(request):

        pageIndex = request.GET.get('pageIndex', 1)
        pageSize = request.GET.get('pageSize', 10)
        name = request.GET.get('name')

        qruery = Q();

        if BaseView.isExit(name):
            qruery = qruery & Q(name__contains=name)

        data = models.Offices.objects.filter(qruery).order_by("-putTime")

        paginator = Paginator(data, pageSize)

        resl = []

        for item in list(paginator.page(pageIndex)):
            temp = {
                'id': item.id,
                'name': item.name,
                'detail': item.detail,
                'putTime': item.putTime,
            }
            resl.append(temp)

        temp = BaseView.parasePage(int(pageIndex), int(pageSize),
                                   paginator.page(pageIndex).paginator.num_pages,
                                   paginator.count, resl)

        return BaseView.successData(temp)

    '''
    添加数据
    '''
    def addInfo(request):

        models.Offices.objects.create(
            name=request.POST.get('name'),
            detail=request.POST.get('detail'),
            putTime=time.strftime("%Y-%m-%d", time.localtime())
        )

        return BaseView.success()

    '''
    修改数据
    '''
    def updInfo(request):

        models.Offices.objects. \
            filter(id=request.POST.get('id')).update(
            name=request.POST.get('name'),
            detail=request.POST.get('detail'),
        )

        return BaseView.success()

    '''
    删除数据
    '''
    def delInfo(request):

        if models.Doctors.objects.filter(office__id=request.POST.get('id')).exists():

            return BaseView.warn('存在关联医师无法移除')
        else:

            models.Offices.objects.filter(id=request.POST.get('id')).delete()
            return BaseView.success()

'''
医师信息
'''
class DoctorsView(BaseView):

    def get(self, request, module, *args, **kwargs):

        if module == 'info':
            return DoctorsView.getInfo(request)
        elif module == 'page':
            return DoctorsView.getPageInfo(request)
        else:
            return BaseView.error()

    def post(self, request, module, *args, **kwargs):

        if module == 'add':
            return DoctorsView.addInfo(request)
        elif module == 'upd':
            return DoctorsView.updInfo(request)
        elif module == 'del':
            return DoctorsView.delInfo(request)
        else:
            return BaseView.error()

    '''
    获取指定数据
    '''
    def getInfo(request):

        data = models.Doctors.objects.filter(id=request.GET.get('id')).first()

        resl = {
            'id': data.id,
            'record': data.record,
            'job': data.job,
            'good': data.good,
            'total': data.total,
            'officeId': data.office.id,
        }

        return BaseView.successData(resl)

    '''
    分页获取数据
    '''
    def getPageInfo(request):

        pageIndex = request.GET.get('pageIndex', 1)
        pageSize = request.GET.get('pageSize', 10)
        name = request.GET.get('name')
        phone = request.GET.get('phone')
        record = request.GET.get('record')
        job = request.GET.get('job')

        qruery = Q();

        if BaseView.isExit(name):
            qruery = qruery & Q(user__name__contains=name)

        if BaseView.isExit(phone):
            qruery = qruery & Q(user__phone__contains=phone)

        if BaseView.isExit(record):
            qruery = qruery & Q(record__contains=record)

        if BaseView.isExit(job):
            qruery = qruery & Q(job__contains=job)

        data = models.Doctors.objects.filter(qruery).order_by("-user__createTime")

        paginator = Paginator(data, pageSize)

        resl = []

        for item in list(paginator.page(pageIndex)):
            temp = {
                'id': item.user.id,
                'userName': item.user.userName,
                'passWord': item.user.passWord,
                'name': item.user.name,
                'gender': item.user.gender,
                'age': item.user.age,
                'phone': item.user.phone,
                'createTime': item.user.createTime,
                'type': item.user.type,
                'record': item.record,
                'job': item.job,
                'good': item.good,
                'total': item.total,
                'officeId': item.office.id,
                'officeName': item.office.name,
            }
            resl.append(temp)

        temp = BaseView.parasePage(int(pageIndex), int(pageSize),
                                   paginator.page(pageIndex).paginator.num_pages,
                                   paginator.count, resl)

        return BaseView.successData(temp)

    '''
    添加数据
    '''
    @transaction.atomic
    def addInfo(request):

        if models.Users.objects.filter(userName=request.POST.get('userName')).exists():

            return BaseView.warn('用户账号已存在无法重复添加')

        user = models.Users.objects.create(
            userName=request.POST.get('userName'),
            passWord=request.POST.get('passWord'),
            name=request.POST.get('name'),
            gender=request.POST.get('gender'),
            age=request.POST.get('age'),
            phone=request.POST.get('phone'),
            type=request.POST.get('type'),
            createTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        )

        models.Doctors.objects.create(
            user=user,
            record=request.POST.get('record'),
            job=request.POST.get('job'),
            good=request.POST.get('good'),
            total=request.POST.get('total'),
            office=models.Offices.objects.get(id=request.POST.get('officeId'))
        )

        return BaseView.success()

    '''
    修改数据
    '''
    def updInfo(request):

        models.Doctors.objects. \
            filter(user__id=request.POST.get('id')).update(
            record=request.POST.get('record'),
            job=request.POST.get('job'),
            good=request.POST.get('good'),
            total=request.POST.get('total'),
            office=models.Offices.objects.filter(id=request.POST.get('officeId')).first()
        )

        return BaseView.success()

    '''
    删除数据
    '''
    @transaction.atomic
    def delInfo(request):

        if models.RegisteLogs.objects.filter(doctor__user__id=request.POST.get('id')).exists():

            return BaseView.warn('存在关联内容无法移除')
        else:

            models.Doctors.objects.filter(user__id=request.POST.get('id')).delete()
            models.Users.objects.filter(id=request.POST.get('id')).delete()

            return BaseView.success()

'''
患者信息
'''
class PatientsView(BaseView):

    def get(self, request, module, *args, **kwargs):

        if module == 'info':
            return PatientsView.getInfo(request)
        elif module == 'page':
            return PatientsView.getPageInfo(request)
        else:
            return BaseView.error()

    def post(self, request, module, *args, **kwargs):

        if module == 'add':
            return PatientsView.addInfo(request)
        elif module == 'upd':
            return PatientsView.updInfo(request)
        elif module == 'del':
            return PatientsView.delInfo(request)
        else:
            return BaseView.error()

    '''
    获取指定数据
    '''
    def getInfo(request):

        data = models.Patients.objects.filter(id=request.GET.get('id')).first()

        resl = {
            'id': data.id,
            'address': data.address,
            'card': data.card
        }

        return BaseView.successData(resl)

    '''
    分页获取数据
    '''
    def getPageInfo(request):

        pageIndex = request.GET.get('pageIndex', 1)
        pageSize = request.GET.get('pageSize', 10)
        name = request.GET.get('name')
        phone = request.GET.get('phone')
        address = request.GET.get('address')

        qruery = Q();

        if BaseView.isExit(name):
            qruery = qruery & Q(user__name__contains=name)

        if BaseView.isExit(name):
            qruery = qruery & Q(user__phone__contains=phone)

        if BaseView.isExit(address):
            qruery = qruery & Q(address__contains=address)

        data = models.Patients.objects.filter(qruery).order_by("-user__createTime")

        paginator = Paginator(data, pageSize)

        resl = []

        for item in list(paginator.page(pageIndex)):
            temp = {
                'id': item.user.id,
                'userName': item.user.userName,
                'passWord': item.user.passWord,
                'name': item.user.name,
                'gender': item.user.gender,
                'age': item.user.age,
                'phone': item.user.phone,
                'createTime': item.user.createTime,
                'type': item.user.type,
                'address': item.address,
                'card': item.card,
            }
            resl.append(temp)

        temp = BaseView.parasePage(int(pageIndex), int(pageSize),
                                   paginator.page(pageIndex).paginator.num_pages,
                                   paginator.count, resl)

        return BaseView.successData(temp)

    '''
    添加数据
    '''
    @transaction.atomic
    def addInfo(request):

        user = models.Users.objects.create(
            userName=request.POST.get('userName'),
            passWord=request.POST.get('passWord'),
            name=request.POST.get('name'),
            gender=request.POST.get('gender'),
            age=request.POST.get('age'),
            phone=request.POST.get('phone'),
            type=request.POST.get('type'),
            createTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        )

        models.Patients.objects.create(
            user=user,
            address=request.POST.get('address'),
            card=request.POST.get('card')
        )

        return BaseView.success()

    '''
    修改数据
    '''
    def updInfo(request):

        models.Patients.objects. \
            filter(id=request.POST.get('id')).update(
            address=request.POST.get('address'),
            card=request.POST.get('card'),
        )

        return BaseView.success()

    '''
    删除数据
    '''
    @transaction.atomic
    def delInfo(request):

        models.RegisteLogs.objects.filter(patient__user__id=request.POST.get('id')).delete()

        models.Patients.objects.filter(user__id=request.POST.get('id')).delete()

        models.Users.objects.filter(id=request.POST.get('id')).delete()

        return BaseView.success()

'''
预约记录
'''
class RegisteLogsView(BaseView):

    def get(self, request, module, *args, **kwargs):

        if module == 'info':
            return RegisteLogsView.getInfo(request)
        elif module == 'page':
            return RegisteLogsView.getPageInfo(request)
        else:
            return BaseView.error()

    def post(self, request, module, *args, **kwargs):

        if module == 'add':
            return RegisteLogsView.addInfo(request)
        elif module == 'upd':
            return RegisteLogsView.updInfo(request)
        elif module == 'del':
            return RegisteLogsView.delInfo(request)
        else:
            return BaseView.error()

    '''
    获取指定数据
    '''
    def getInfo(request):

        data = models.RegisteLogs.objects.filter(id=request.GET.get('id')).first()

        resl = {
            'id': data.id,
            'registeTime': data.registeTime,
            'createTime': data.createTime,
            'total': data.total,
            'status': data.status,
            'patientId': data.patient.user.id,
            'doctorId': data.doctor.user.id,
        }

        return BaseView.successData(resl)

    '''
    分页获取数据
    '''
    def getPageInfo(request):

        loginUser = SysView.getLoginUser(request.GET.get('token'))

        pageIndex = request.GET.get('pageIndex', 1)
        pageSize = request.GET.get('pageSize', 10)
        doctorName = request.GET.get('doctorName')
        paientName = request.GET.get('paientName')

        qruery = Q();

        if loginUser['type'] == 1:
            qruery = qruery & Q(doctor__user__id=loginUser['id'])

        if loginUser['type'] == 2:
            qruery = qruery & Q(patient__user__id=loginUser['id'])

        if BaseView.isExit(doctorName):
            qruery = qruery & Q(doctor__user__name__contains=doctorName)

        if BaseView.isExit(paientName):
            qruery = qruery & Q(patient__user__title__contains=paientName)

        data = models.RegisteLogs.objects.filter(qruery).order_by("-createTime")

        paginator = Paginator(data, pageSize)

        resl = []

        for item in list(paginator.page(pageIndex)):
            temp = {
                'id': item.id,
                'registeTime': item.registeTime,
                'createTime': item.createTime,
                'total': item.total,
                'status': item.status,
                'patientId': item.patient.user.id,
                'patientName': item.patient.user.name,
                'patientGender': item.patient.user.gender,
                'patientAge': item.patient.user.age,
                'patientPhone': item.patient.user.phone,
                'patientAddress': item.patient.address,
                'patientCard': item.patient.card,
                'doctorId': item.doctor.user.id,
                'doctorJob': item.doctor.job,
                'doctorPhone': item.doctor.user.phone,
                'doctorName': item.doctor.user.name,
                'doctorOfficeName': item.doctor.office.name,
            }
            resl.append(temp)

        temp = BaseView.parasePage(int(pageIndex), int(pageSize),
                                   paginator.page(pageIndex).paginator.num_pages,
                                   paginator.count, resl)

        return BaseView.successData(temp)

    '''
    添加数据
    '''
    def addInfo(request):

        user = SysView.getLoginUser(request.POST.get('token'))

        qruery = Q()
        qruery = qruery & Q(patient__user__id=user['id'])
        qruery = qruery & Q(doctor__user__id=request.POST.get('doctorId'))
        qruery = qruery & Q(registeTime=request.POST.get('registeTime'))

        if models.RegisteLogs.objects.filter(qruery).exists():

            return BaseView.warn('预约记录已存在')
        else:
            models.RegisteLogs.objects.create(
                total=request.POST.get('total'),
                status=request.POST.get('status'),
                registeTime=request.POST.get('registeTime'),
                createTime=time.strftime("%Y-%m-%d", time.localtime()),
                patient=models.Patients.objects.filter(user__id=user['id']).first(),
                doctor=models.Doctors.objects.filter(user__id=request.POST.get('doctorId')).first()
            )

            return BaseView.success()

    '''
    修改数据
    '''
    def updInfo(request):

        models.RegisteLogs.objects. \
            filter(id=request.POST.get('id')).update(
            status=request.POST.get('status'),
        )

        return BaseView.success()

    '''
    删除数据
    '''
    def delInfo(request):

        models.RegisteLogs.objects.filter(id=request.POST.get('id')).delete()

        return BaseView.success()
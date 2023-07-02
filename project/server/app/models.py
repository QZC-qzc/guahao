from django.db import models

# 通知信息
class Notices(models.Model):
    id = models.AutoField('记录编号', primary_key=True)
    title = models.CharField('通知标题',  max_length=32, null=False)
    detail = models.CharField('通知详情', max_length=125, null=False)
    putTime = models.CharField('通知时间', db_column='put_time', max_length=10)
    class Meta:
        db_table = 'notices'

# 科室信息
class Offices(models.Model):
    id = models.AutoField('记录编号', primary_key=True)
    name = models.CharField('科室名称',  max_length=32, null=False)
    detail = models.CharField('通知详情', max_length=125, null=False)
    putTime = models.CharField('通知时间', db_column='put_time', max_length=10)
    class Meta:
        db_table = 'offices'

# 账号信息
class Users(models.Model):
    id = models.AutoField('记录编号', primary_key=True)
    userName = models.CharField('用户账号', db_column='user_name', max_length=32, null=False)
    passWord = models.CharField('用户密码', db_column='pass_word', max_length=32, null=False)
    name = models.CharField('用户姓名', max_length=20, null=False)
    gender = models.CharField('用户性别', max_length=2, null=False)
    age = models.IntegerField('用户年龄', null=False)
    phone = models.CharField('联系电话', max_length=11, null=False)
    createTime = models.CharField('添加时间', db_column='create_time', max_length=19)
    type = models.IntegerField('用户身份', null=False)
    class Meta:
        db_table = 'users'

# 医师信息
class Doctors(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, db_column="id", primary_key=True)
    record = models.CharField('医师学历',  max_length=32, null=False)
    job = models.CharField('医师职称', max_length=20, null=False)
    good = models.CharField('专长描述', max_length=125, null=False)
    total = models.FloatField('挂号费用', null=False)
    office = models.ForeignKey(Offices, on_delete=models.CASCADE, db_column="office_id")
    class Meta:
        db_table = 'doctors'

# 患者信息
class Patients(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, db_column="id", primary_key=True)
    address = models.CharField('联系地址',  max_length=64, null=False)
    card = models.CharField('身份证号', max_length=18, null=False)
    class Meta:
        db_table = 'patients'

# 挂号记录
class RegisteLogs(models.Model):
    id = models.AutoField('记录编号', primary_key=True)
    registeTime = models.CharField('预约时间', db_column='registe_time', max_length=10)
    createTime = models.CharField('提交时间', db_column='create_time', max_length=10)
    total = models.FloatField('挂号费用', null=False)
    status = models.IntegerField('挂号状态', null=False)
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, db_column="patient_id")
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE, db_column="doctor_id")
    class Meta:
        db_table = 'registe_logs'
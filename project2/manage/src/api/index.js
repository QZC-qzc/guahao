import http from "../utils/http.js";

/** 系统接口 */
export function getStatis(token){
	
	return http.get('/statis/');
}
export function login(param){
	
	return http.post('/login/', param);
}
export function exit(token){
	
	return http.get('/exit/', {params: token});
}
export function getLoginUser(token){
	
	return http.get('/info/', {params: {token: token}});
}
export function checkUserPwd(token, oldPwd){
	
	return http.get('/checkPwd/', {params: {token: token, oldPwd: oldPwd}});
}
export function updLoginUserInfo(params){
	
	return http.post('/info/', params);
}
export function updLoginUserPwd(token, newPwd){
	
	return http.post('/pwd/', {token: token, newPwd: newPwd});
}

/** 通知信息接口 */
export function getTopNotices(){

	return http.get('/notices/top/');
}
export function getPageNotices(pageIndex, pageSize, title){

	return http.get('/notices/page/', 
        {params: {pageIndex: pageIndex, pageSize: pageSize, title: title}});
}
export function addNotices(params){
	
	return http.post('/notices/add/', params);
}
export function updNotices(params){
	
	return http.post('/notices/upd/', params);
}
export function delNotices(id){
	
	return http.post('/notices/del/', {id: id});
}

/** 科室信息接口 */
export function getAllOffices(){

	return http.get('/offices/all/');
}
export function getPageOffices(pageIndex, pageSize, name){

	return http.get('/offices/page/', 
        {params: {pageIndex: pageIndex, pageSize: pageSize, name: name}});
}
export function addOffices(params){
	
	return http.post('/offices/add/', params);
}
export function updOffices(params){
	
	return http.post('/offices/upd/', params);
}
export function delOffices(id){
	
	return http.post('/offices/del/', {id: id});
}

/** 医师信息接口 */
export function getPageDoctors(pageIndex, pageSize, name, phone, record, job){

	return http.get('/doctors/page/', 
        {params: {pageIndex: pageIndex, pageSize: pageSize, name: name, phone: phone, record: record, job: job}});
}
export function addDoctors(params){
	
	return http.post('/doctors/add/', params);
}
export function updDoctors(params){
	
	return http.post('/doctors/upd/', params);
}
export function delDoctors(id){
	
	return http.post('/doctors/del/', {id: id});
}

/** 患者信息接口 */
export function getPagePatients(pageIndex, pageSize, name, phone, address){

	return http.get('/patients/page/', 
        {params: {pageIndex: pageIndex, pageSize: pageSize, name: name, phone: phone, address: address}});
}
export function addPatients(params){
	
	return http.post('/patients/add/', params);
}
export function updPatients(params){
	
	return http.post('/patients/upd/', params);
}
export function delPatients(id){
	
	return http.post('/patients/del/', {id: id});
}

/** 预约记录接口 */
export function getPageRegistes(pageIndex, pageSize, token, doctorName, paientName){

	return http.get('/registes/page/', 
        {params: {pageIndex: pageIndex, pageSize: pageSize, token: token, doctorName: doctorName, paientName: paientName}});
}
export function addRegistes(params){
	
	return http.post('/registes/add/', params);
}
export function updRegistes(params){
	
	return http.post('/registes/upd/', params);
}
export function delRegistes(id){
	
	return http.post('/registes/del/', {id: id});
}


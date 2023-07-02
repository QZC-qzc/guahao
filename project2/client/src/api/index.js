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

/** 医师信息接口 */
export function getPageDoctors(pageIndex, pageSize){

	return http.get('/doctors/page/', 
        {params: {pageIndex: pageIndex, pageSize: pageSize}});
}

/** 患者信息接口 */
export function addPatients(params){
	
	return http.post('/patients/add/', params);
}

/** 预约记录接口 */
export function getPageRegistes(pageIndex, pageSize, token){

	return http.get('/registes/page/', 
        {params: {pageIndex: pageIndex, pageSize: pageSize, token: token}});
}
export function addRegistes(params){
	
	return http.post('/registes/add/', params);
}
export function updRegistes(params){
	
	return http.post('/registes/upd/', params);
}
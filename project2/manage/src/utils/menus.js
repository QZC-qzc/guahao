import {getLoginUser} from "../api";

// 系统管理员
export const adminMenus = {
    path: '/home',
    name: 'home',
    component: require("../views/home.vue").default,
    children: [
        {
            path: '/welcome',
            name: '系统首页',
            icon: "fa fa-home",
            component: require("../views/pages/welcome.vue").default
        },
        {
            path: '/notices',
            name: '系统通知管理',
            icon: "fa fa-bullhorn",
            component: require("../views/pages/notices.vue").default
        },
        {
            path: '/offices',
            name: '科室信息管理',
            icon: "fa fa-bookmark",
            component: require("../views/pages/offices.vue").default
        },
        {
            path: '/doctors',
            name: '医师信息管理',
            icon: "fa fa-users",
            component: require("../views/pages/doctors.vue").default
        },
        {
            path: '/patients',
            name: '患者信息管理',
            icon: "fa fa-address-card",
            component: require("../views/pages/patients.vue").default
        },
        {
            path: '/registes',
            name: '挂号记录管理',
            icon: "fa fa-map-o",
            component: require("../views/pages/registes.vue").default
        }
    ]
};

export const docMenus = {
    path: '/home',
    name: 'home',
    component: require("../views/home.vue").default,
    children: [
        {
            path: '/welcome',
            name: '系统首页',
            icon: "fa fa-home",
            component: require("../views/pages/welcome.vue").default
        },
        {
            path: '/registes',
            name: '挂号记录管理',
            icon: "fa fa-map-o",
            component: require("../views/pages/registes.vue").default
        }
    ]
};

export default function initMenu(router, store){
	
    let token = null;
    if(store.state.token){

        token = store.state.token;
    }else{

        token = sessionStorage.getItem("token");
        store.state.token = sessionStorage.getItem("token");
    }

    getLoginUser(token).then(resp =>{

        if(resp.data.type == 0){
            router.addRoute(adminMenus);
            store.commit("setMenus", adminMenus);
        }
    
        if(resp.data.type == 1){
            router.addRoute(docMenus);
            store.commit("setMenus", docMenus);
        }
    });
}



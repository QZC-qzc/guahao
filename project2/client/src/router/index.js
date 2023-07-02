import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'index',
    component: require('../views/index.vue').default,
    children: [
      {
        path: '/welcome',
        name: 'welcome',
        component: require('../views/welcome.vue').default
      },
      {
        path: '/list',
        name: 'list',
        component: require('../views/list.vue').default
      },
      {
        path: '/user',
        name: 'user',
        component: require('../views/user.vue').default
      }
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router
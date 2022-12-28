import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../../../views/HomeView.vue'
import UserInfo from "@/module/User/UserInfo.vue";
import UserSetting from "@/module/User/UserSetting";
import UserUpdate from "@/module/User/UserUpdate";


const routes = [
  // {
  //   path: '/',
  //   name: 'home',
  //   component: HomeView
  // },
  {
    path:'/UserInfo',
    name:'UserInfo',
    component: UserInfo,
    alias:'/',
  },
   {
    path:'/UserSetting',
    name:'UserSetting',
    component: UserSetting,
  },
   {
    path:'/UserUpdate',
    name:'UserUpdate',
    component: UserUpdate,
  },
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../../../views/AboutView.vue')
  // },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})



export default router

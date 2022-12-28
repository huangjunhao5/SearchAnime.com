import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '@/module/MainPage/Home.vue';
import AnimePage from '@/module/MainPage/AnimePage.vue'
import RankPage from "@/module/MainPage/RankPage.vue";
import NewCommentPage from "@/module/MainPage/NewCommentPage.vue";
import FindAnimePage from "@/module/MainPage/FindAnimePage.vue"
import SearchResultPage from "@/module/MainPage/SearchResultPage.vue";

const routes = [
  {
    path: '/home',
    name: 'home',
    component: Home,
    alias:'/',
  },
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // },
  {
    path: '/AnimePage',
    name: 'AnimePage',
    component: AnimePage,
  },
  {
    path: '/FindAnimePage',
    name: 'FindAnimePage',
    component: FindAnimePage,
  },
  {
    path: '/RankPage',
    name: 'RankPage',
    component: RankPage,
  },
  {
    path: '/NewCommentPage',
    name: 'NewCommentPage',
    component: NewCommentPage,
  },
  {
    path: '/SearchResultPage',
    name: 'SearchResultPage',
    component: SearchResultPage,
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

export default router

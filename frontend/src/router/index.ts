import type { RouteRecordRaw, Router } from 'vue-router'
import { createRouter, createWebHistory } from 'vue-router'
import { EAppRouteNames, EAppRoutePaths } from '#/types/routes'

const Home = import('#/views/home-view.vue')

const routes: RouteRecordRaw[] = [
  {
    path: EAppRoutePaths.Home,
    name: EAppRouteNames.Home,
    component: Home,
  },
]

const router: Router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router

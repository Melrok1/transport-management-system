import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import OrdersListView from '@/views/OrdersListView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/ordersListView',
    name: 'ordersListView',
    component: OrdersListView
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router

import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import OrdersListView from '@/views/OrdersListView.vue'
import OrderDetailView from '@/views/OrderDetailView.vue'

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
  },
  {
  path: '/orders/:id',
  name: 'OrderDetail',
  component: OrderDetailView
}
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router

import Vue from 'vue'
import VueRouter from 'vue-router'
import BottomUpView from '@/views/BottomUpView.vue'
import TopDownView from '@/views/TopDownView.vue'
import ManagerView from '@/views/ManagerView.vue'
import AdminView from '@/views/AdminView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'bottom-up',
    component: BottomUpView
  },
  {
    path: '/manager',
    name: 'manager',
    component: ManagerView
  },
  {
    path: '/top-down',
    name: 'top-down',
    component: TopDownView
  },
  {
    path: '/admin',
    name: 'admin',
    component: AdminView
  }
]

const router = new VueRouter({
  routes
})

export default router

import Vue from 'vue'
import VueRouter from 'vue-router'
import BottomUpView from '@/views/BottomUpView.vue'
import TopDownView from '@/views/TopDownView.vue'
import ManagerView from '@/views/ManagerView.vue'
import AdminView from '@/views/AdminView.vue'
import Login from '@/components/Login'
import store from '@/store'

Vue.use(VueRouter)

const ifAuthenticated = (to, from, next) => {
	if (store.getters.isAuthenticated) {
		return next();
	}
	return next('/login');
};

const routes = [
  {
    path: '/bottom-up',
    name: 'bottom-up',
    component: BottomUpView,
    // beforeEnter (to, from, next) {
    //   if (!store.getters.isAuthenticated) {
    //     next('/login')
    //   } else {
    //     next()
    //   }
    // }
    
    // beforeEnter: (to, from, next) => {
		// 	ifAuthenticated(to, from, next);
		// },
  },
  {
    path: '/manager',
    name: 'manager',
    component: ManagerView,
    // beforeEnter: (to, from, next) => {
		// 	ifAuthenticated(to, from, next);
		// },
  },
  {
    path: '/top-down',
    name: 'top-down',
    component: TopDownView,
    // beforeEnter: (to, from, next) => {
		// 	ifAuthenticated(to, from, next);
		// },
  },
  {
    path: '/admin',
    name: 'admin',
    component: AdminView,
    // beforeEnter: (to, from, next) => {
		// 	ifAuthenticated(to, from, next);
		// },
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/',
		name: 'Home',
		redirect: '/login'
  }
]

const router = new VueRouter({
  routes
})

export default router

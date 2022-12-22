import Vue from "vue";
import VueRouter from "vue-router";
import Dashboard from "@/views/Dashboard/index.vue";
import BottomUpView from "@/views/Dashboard/BottomUpView.vue";
import TopDownView from "@/views/Dashboard/TopDownView.vue";
import ManagerView from "@/views/Dashboard/ManagerView.vue";
import AdminView from "@/views/Dashboard/AdminView.vue";
import Login from "@/views/Login";
import store from "@/store";

Vue.use(VueRouter);

const ifAuthenticated = (to, from, next) => {
  if (store.getters.isAuthenticated) {
    return next();
  }
  return next("/login");
};

const routes = [
  {
    path: "/dashboard",
    alias: "/",
    name: "Dashboard",
    component: Dashboard,
    redirect: "/dashboard/bottom-up",
    children: [
      {
        path: "/dashboard/bottom-up",
        name: "DashboardBottomUp",
        component: BottomUpView,
        beforeEnter: (to, from, next) => ifAuthenticated(to, from, next),
      },
      {
        path: "/dashboard/manager",
        name: "DashboardManager",
        component: ManagerView,
        beforeEnter: (to, from, next) => ifAuthenticated(to, from, next),
      },
      {
        path: "/dashboard/top-down",
        name: "DashboardTop-Down",
        component: TopDownView,
        beforeEnter: (to, from, next) => ifAuthenticated(to, from, next),
      },
      {
        path: "/dashboard/admin",
        name: "DashboardAdmin",
        component: AdminView,
        beforeEnter: (to, from, next) => ifAuthenticated(to, from, next),
      },
    ],
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "*",
    redirect: "/dashboard",
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;

import Vue from "vue"
import VueRouter from "vue-router"
import Randoms from "@/views/Randoms.vue"

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Randoms
  },
  {
    path: "/folders",
    name: "folders",
    props: true,
    component: () =>
      import(/* webpackChunkName: "folders" */ "@/views/Folders.vue")
  },
  {
    path: "/full_list/:start_index",
    name: "full_list",
    props: true,
    component: () =>
      import(/* webpackChunkName: "explorer" */ "@/views/Full_List.vue")
  },
  {
    path: "/explorer/:start_index",
    name: "explorer",
    props: true,
    component: () =>
      import(/* webpackChunkName: "explorer" */ "@/views/Explorer.vue")
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
})

export default router

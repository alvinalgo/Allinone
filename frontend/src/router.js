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
      import(/* webpackChunkName: "full_list" */ "@/views/Full_List.vue")
  },
  {
    path: "/explorer/:target_index/:start_index",
    name: "explorer",
    props: true,
    component: () =>
      import(/* webpackChunkName: "explorer" */ "@/views/Explorer.vue")
  },
  {
    path: "/tag/:tag",
    name: "tag",
    props: true,
    component: () =>
      import(/* webpackChunkName: "tag" */ "@/views/Tag.vue")
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
})

export default router

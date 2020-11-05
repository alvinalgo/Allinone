import Vue from "vue"
import VueRouter from "vue-router"

Vue.use(VueRouter);

const routes = [
  {
    path: "/:start_index?",
    name: "Home",
    component: () =>
    import(/* webpackChunkName: "Home" */ "@/views/Home.vue")
  },
  {
    path: "/folders/:folder_id/:start_index?",
    name: "Folders",
    props: true,
    component: () =>
      import(/* webpackChunkName: "folders" */ "@/views/Folders.vue")
  },
  {
    path: "/full_list/:start_index?",
    name: "Full List",
    props: true,
    component: () =>
      import(/* webpackChunkName: "full_list" */ "@/views/Full_List.vue")
  },
  {
    path: "/explorer/:target_index/:start_index?",
    name: "Explorer",
    props: true,
    component: () =>
      import(/* webpackChunkName: "explorer" */ "@/views/Explorer.vue")
  },
  {
    path: "/tags/:tag?",
    name: "Tags",
    props: true,
    component: () =>
      import(/* webpackChunkName: "tag" */ "@/views/Tags.vue")
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
})

export default router

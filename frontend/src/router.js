import Vue from "vue"
import VueRouter from "vue-router"

Vue.use(VueRouter);

const routes = [
  {
    path: "/:startIndex?",
    name: "Home",
    component: () =>
    import(/* webpackChunkName: "Home" */ "@/views/Home.vue")
  },
  {
    path: "/folders/:folderId/:startIndex?",
    name: "Folders",
    props: true,
    component: () =>
      import(/* webpackChunkName: "folders" */ "@/views/Folders.vue")
  },
  {
    path: "/full_list/:startIndex?",
    name: "Full List",
    props: true,
    component: () =>
      import(/* webpackChunkName: "full_list" */ "@/views/Full_List.vue")
  },
  {
    path: "/explorer/:targetIndex/:startIndex?",
    name: "Explorer",
    props: true,
    component: () =>
      import(/* webpackChunkName: "explorer" */ "@/views/Explorer.vue")
  },
  {
    path: "/tags/:clusteringMethod/:tag?/:startIndex?",    //  /tags/:tag?/:startIndex?
    name: "Tags",
    props: true,
    component: () =>
      import(/* webpackChunkName: "tag" */ "@/views/Tags.vue"),
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
})

export default router

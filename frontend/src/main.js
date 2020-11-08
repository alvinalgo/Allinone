import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import VueMaterial from 'vue-material'    // import { MdCard } from 'vue-material/dist/components'
var infiniteScroll =  require('vue-infinite-scroll');
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

// Vue.config.devtools = true;
// Vue.config.productionTip = false;

Vue.use(VueMaterial)    // Vue.use(MdCard)
Vue.use(infiniteScroll)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
import Vue from "vue"
import Vuex from "vuex"

import axios from "axios"

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    loaded: {
      folders: false,
      full_list: false
    },
    folders: [],
    bookmark_bar: []
  },
  mutations: {
    update_folder(state, payload){
      state.folders = payload
    },
    update_full_list(state, payload){
      // console.log(payload)  //eslint-disable-line
      state.bookmark_bar = payload
    }

  },
  actions: {
    check_folders({commit}) {
      if (!this.state.loaded.folders) {
        axios.get('http://127.0.0.1:5000/folders')
          .then(response => {
            commit('update_folder', response.data)
        })
        this.state.loaded.folders = true
      }
    },
    check_full_list({commit}) {
      if (!this.state.loaded.full_list) {
        axios.get('http://127.0.0.1:5000/full_list')
          .then(response => {
            commit('update_full_list', response.data)
        })
        this.state.loaded.full_list = true
      }
    },
  },
  modules: {}
})
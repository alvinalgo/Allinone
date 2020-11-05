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
    display: {
      display_style: 'fountain_display',
      sorting: 'recents'
    },
    folders: [],
    sorted_all_bookmarks: [],
    folder_stack: [],
  },
  mutations: {
    update_folder(state, payload) {
      state.folders = payload
    },
    update_full_list(state, payload) {
      state.sorted_all_bookmarks = payload
    },

    stack_the_folder(state, payload) {
      state.folder_stack.push(payload)
    },
    update_folder_stack(state, payload) {
      state.folder_stack = state.folder_stack.slice(0, payload+1)
    },
    refresh_folder_stack(state, payload) {
      state.folder_stack = payload
    },

    update_display(state, payload) {
      state.display['display_style'] = payload
    },
    update_sorting(state, payload) {
      state.display['sorting'] = payload
    }
  },
  actions: {
    check_folders({commit}) {
      if (!this.state.loaded.folders) {
        axios.get('http://127.0.0.1:5000/folders')
          .then(response => {
            commit('update_folder', response.data)
        })
        this.state.loaded.folders = true    // 待改，要用 mutation
      }
    },
    check_full_list({commit}) {
      if (!this.state.loaded.full_list) {
        axios.get('http://127.0.0.1:5000/full_list')
          .then(response => {
            commit('update_full_list', response.data)
        })
        this.state.loaded.full_list = true    // 待改，要用 mutation
      }
    },

    stack_the_folder({commit}, payload) {
      commit('stack_the_folder', payload)
    }, 
    update_folder_stack({commit}, payload) {
      commit('update_folder_stack', payload)
    },
    refresh_folder_stack({commit}, payload) {
      if (payload === '-1') {
        commit('update_folder_stack', -1)
      }
      else {
        axios.get('http://127.0.0.1:5000/get_parents_and_self/'+payload)
            .then(response => {
              commit('refresh_folder_stack', response.data)
          })
      }
    },

    update_display({commit}, payload) {
      commit('update_display', payload)
    },
    update_sorting({commit}, payload) {
      commit('update_sorting', payload)
    },
  },
  modules: {}
})
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
      display_style: 'grid_display',
      sorting: 'recents',
      displayingSize: 30,
      clusterMethod: 'word_tokenized'
    },
    // folders: [],
    // sorted_all_bookmarks: [],
    folder_stack: [],
    displayingInfoId: false
  },
  mutations: {
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
    },
    updateClusterMethod(state, payload) {
      state.display['clusterMethod'] = payload
    },

    updateInfoId (state, payload) {
      state.displayingInfoId = payload
    }
  },
  actions: {

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

    update_display ({commit}, payload) {
      commit('update_display', payload)
    },
    update_sorting ({commit}, payload) {
      commit('update_sorting', payload)
    },
    updateClusterMethod ({commit}, payload) {
      commit('updateClusterMethod', payload)
    },

    updateInfoId ({commit}, payload) {
      commit('updateInfoId', payload)
    }
  },
  modules: {}
})
<template>
  <div class="view-wrapper">
    <h1>Explorer</h1>
      <div>
        <a @click.prevent="redirect_to_root_and_reset_folder_stack">Home</a>
        <span v-for="(stack, i) in this.$store.state.folder_stack" :key="stack.id">
          &gt;
          <a @click.prevent="redirect_page(i)">
            {{stack.name}}
          </a>
        </span>
      </div>
      
    <PagingSystem :bookmarks="bookmarks"/>
  </div>
</template>

<script>
import axios from "axios"
import PagingSystem from "../components/paging_system"

export default {
  name: "folders",
  components: {
    PagingSystem
  },
  data () {
    return {
      bookmarks: []
    }
  },
  methods: {
    redirect_page (index_in_stack) {
      this.$store.dispatch('update_folder_stack', index_in_stack)
      var target_index = this.$store.state.folder_stack[index_in_stack]['id']
      this.$router.push({name:'explorer', params:{'target_index':target_index, 'start_index':0}}).catch(()=>{})
    },
    redirect_to_root_and_reset_folder_stack () {
      this.$store.dispatch('update_folder_stack', -1)
      this.$router.push({name:'explorer', params:{'target_index':'-1', 'start_index':0}}).catch(()=>{})
    }
  },
  mounted () {
    if (this.$route.params.target_index) {
      axios.get('http://127.0.0.1:5000/explorer_query/'+this.$route.params.target_index)
      .then(response => {
        this.bookmarks = response.data
      })

      if ((this.$store.state.folder_stack.length && this.$store.state.folder_stack.slice(-1)[0]['id'] !== this.$route.params.target_index) ||
          (!this.$store.state.folder_stack.length && this.$route.params.target_index !== '-1')
      ) {
        this.$store.dispatch('refresh_folder_stack', this.$route.params.target_index)
      }
    }
    else {    //
      axios.get('http://127.0.0.1:5000/explorer_query/-1')
      .then(response => {
        this.bookmarks = response.data
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.view-wrapper {
  width: 90%;
  margin: 0 auto;
}
</style>
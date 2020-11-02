<template>
  <div class="view-wrapper">
    <h1>Explorer</h1>
    <div class="align">
      <div>
        <a @click.prevent="redirect_to_root_and_reset_folder_stack">Home</a>
        <span v-for="(stack, i) in this.$store.state.folder_stack" :key="stack.id">
          >
          <!-- <router-link :to="{name:'explorer', params:{'start_index': 0, 'target_index': stack.id}}"> -->
          <a @click.prevent="redirect_page(i)">
            {{stack.name}}
          </a>
          <!-- </router-link> -->
        </span>
      </div>
      
      <md-button class="md-dense md-raised" :to="{name: 'explorer', params: {start_index: valid_page(false)}}">&lt;</md-button>
      <md-button class="md-dense md-raised" :to="{name: 'explorer', params: {start_index: valid_page(true)}}">&gt;</md-button>
      
      {{ start_index }} - {{ start_index + 20 }}
    </div>
    <Display :images="get_displaying_slice()"/>
  </div>
</template>

<script>
import axios from "axios"
import Display from "../components/grid_display"

export default {
  name: "folders",
  components: {
    Display
  },
  data () {
    return {
      bookmark: []
    }
  },
  computed: {
    start_index(){
      var index = this.$route.params.start_index
      return index ? parseInt(index) : 0
    }
  },
  methods: {
    get_displaying_slice () {
      return this.bookmark.slice(this.start_index, this.start_index + 20)
    },
    valid_page (is_next_page) {
      if (is_next_page) {
        return this.start_index+20 > this.bookmark.length ?
          this.start_index : this.start_index+20
      }
      else {
        return Math.max(this.start_index-20, 0)
      }
    },
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
        this.bookmark = response.data
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
        this.bookmark = response.data
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

.align {
  display: flex;
  align-items: baseline;
}

.md-ripple {
  margin: 10px 0px;
}
</style>
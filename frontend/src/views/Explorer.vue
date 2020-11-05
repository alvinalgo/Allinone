<template>
  <div>
    <div class="flex-wrapper">
      <div>
        <a @click.prevent="redirect_to_root_and_reset_folder_stack">Home</a>
        <span v-for="(stack, i) in this.$store.state.folder_stack" :key="stack.id">
          &gt;
          <a @click.prevent="redirect_page(i)">
            {{stack.name}}
          </a>
        </span>
      </div>
      <PerformingOptions/>
    </div>
    <DisplaySystem :card_list="bookmarks" :click_card_head="click_card_head"/>
  </div>
</template>

<script>
import axios from "axios"
import DisplaySystem from "@/components/display_system/index"
import PerformingOptions from "@/components/display_system/performing_options"

export default {
  name: "folders",
  components: {
    DisplaySystem,
    PerformingOptions
  },
  data () {
    return {
      bookmarks: [],
    }
  },
  methods: {
    redirect_page (index_in_stack) {
      this.$store.dispatch('update_folder_stack', index_in_stack)
      var target_index = this.$store.state.folder_stack[index_in_stack]['id']
      this.$router.push({name:'Explorer', params:{'target_index':target_index, 'start_index':0}}).catch(()=>{})
    },
    redirect_to_root_and_reset_folder_stack () {
      this.$store.dispatch('update_folder_stack', -1)
      this.$router.push({name:'Explorer', params:{'target_index':'-1', 'start_index':0}}).catch(()=>{})
    },
    click_card_head (bookmarks) {
      if(bookmarks['type'] == 'folder') {
        this.$store.dispatch('stack_the_folder', bookmarks)
        this.$router.push({params:{target_index:bookmarks['id'], start_index:0}})
      }
      else {
        window.open(bookmarks['url'], "_blank")
      }
    }
  },
  mounted () {
    if (this.$route.params.target_index) {
      axios.get('http://127.0.0.1:5000/query_a_folder/'+this.$route.params.target_index)
      .then(response => {
        this.bookmarks = response.data['children']
      })

      if ((this.$store.state.folder_stack.length && this.$store.state.folder_stack.slice(-1)[0]['id'] !== this.$route.params.target_index) ||
          (!this.$store.state.folder_stack.length && this.$route.params.target_index !== '-1')
      ) {
        this.$store.dispatch('refresh_folder_stack', this.$route.params.target_index)
      }
    }
    else {
      axios.get('http://127.0.0.1:5000/query_a_folder/-1')
      .then(response => {
        this.bookmarks = response.data['children']
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.flex-wrapper {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
}
</style>
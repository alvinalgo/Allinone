<template>
  <ViewTemplate>
    <template #control-panel>
      <div>
        <a @click.prevent="redirect_to_root_and_reset_folder_stack">Home</a>
        <span v-for="(stack, i) in folder_stack" :key="stack.id">
          &gt;
          <a @click.prevent="redirect_page(i)">
            {{stack.name}}
          </a>
        </span>
      </div>
      <PerformingOptions/>
    </template>
    <template #result-display>
      <DisplaySystem :card_list="bookmarks" :CardComponent="CardComponent" />
    </template>
  </ViewTemplate>
</template>

<script>
import axios from "axios"
import Card from "@/components/display_system/cards/explorerCard"
import DisplaySystem from "@/components/display_system/index"
import PerformingOptions from "@/components/display_system/performing_options"
import ViewTemplate from "@/components/TheViewTemplate"


export default {
  name: "folders",
  components: {
    ViewTemplate,
    DisplaySystem,
    PerformingOptions
  },
  data () {
    return {
      bookmarks: [],
      CardComponent: Card,
    }
  },
  computed: {
    folder_stack () { return this.$store.state.folder_stack }
  },
  methods: {
    redirect_page (index_in_stack) {
      this.$store.dispatch('update_folder_stack', index_in_stack)
      var targetIndex = this.$store.state.folder_stack[index_in_stack]['id']
      this.$router.push({name:'Explorer', params:{'targetIndex':targetIndex, 'startIndex':0}}).catch(()=>{})
    },
    redirect_to_root_and_reset_folder_stack () {
      this.$store.dispatch('update_folder_stack', -1)
      this.$router.push({name:'Explorer', params:{'targetIndex':'-1', 'startIndex':0}}).catch(()=>{})
    }
  },
  mounted () {
    if (this.$route.params.targetIndex) {
      console.log('mounted', this.$route.params)

      axios.get('http://127.0.0.1:5000/query_a_folder/'+this.$route.params.targetIndex)
      .then(response => {
        this.bookmarks = response.data['children']
      })

      if ((this.$store.state.folder_stack.length && this.$store.state.folder_stack.slice(-1)[0]['id'] !== this.$route.params.targetIndex) ||
        (!this.$store.state.folder_stack.length && this.$route.params.targetIndex !== '-1')) {
        console.log('refreshing folder_stack')
        this.$store.dispatch('refresh_folder_stack', this.$route.params.targetIndex)
      }

    } else {
      axios.get('http://127.0.0.1:5000/query_a_folder/-1')
      .then(response => {
        console.log('no targetIndex (targetIndex == -1)')
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
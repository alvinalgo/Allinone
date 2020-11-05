<template>
  <div>
    <div class="flex-wrapper">
      <h2>{{ name }}</h2>
      <PerformingOptions/>
    </div>
    <DisplaySystem :card_list="card_list" :click_card_head="click_card_head"/>
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
      card_list: [],
      name: ''
    }
  },
  mounted() {
    if (this.$route.params.tag === '-1') {
      axios.get('http://127.0.0.1:5000/tags')
        .then(response => {
          this.name = 'All tags'
          this.card_list = response.data
      })
    } else {
      axios.get(`http://127.0.0.1:5000/query_a_tag/word_tokenized/${this.$route.params.tag}`)
        .then(response => {
          this.name = response.data['name']
          this.card_list = response.data['children']
      })
    }
  },
  methods: {
    click_card_head (bookmarks) {
      if(bookmarks['type'] == 'folder') {
        this.$router.push({name: 'Folders', params:{folder_id: bookmarks['id'], start_index: '0'}})
      }
      else {
        window.open(bookmarks['url'], "_blank")
      }
    }
  }
}
</script>

<style lang="scss">
.flex-wrapper {
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-between;
  align-items: center;
}
</style>

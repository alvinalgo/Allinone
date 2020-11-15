<template>
  <ViewTemplate>
    <template #control-panel>
      <h2>{{ folder_name }}</h2>
      <PerformingOptions />
    </template>
    <template #result-display>
      <DisplaySystem :card_list="card_list" :CardComponent="CardComponent" />
    </template>
  </ViewTemplate>
</template>

<script>
import axios from "axios"
import DisplaySystem from "@/components/display_system/index"
import PerformingOptions from "@/components/display_system/performing_options"
import Card from "@/components/display_system/cards/nonExplorerCard"
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
      card_list: [],
      folder_name: '',
      CardComponent: Card,
    }
  },
  mounted() {
    if (this.$route.params.folderId === '-1') {
      axios.get('http://127.0.0.1:5000/folders')
        .then(response => {
          this.folder_name = 'All folders'
          this.card_list = response.data
      })
    } else {
      axios.get(`http://127.0.0.1:5000/query_a_folder/${this.$route.params.folderId}`)
        .then(response => {
          this.folder_name = response.data['name']
          this.card_list = response.data['children']
      })
    }
  }
}
</script>
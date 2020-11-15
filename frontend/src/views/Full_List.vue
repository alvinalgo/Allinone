<template>
  <ViewTemplate>
    <template #control-panel>
      <div />
      <PerformingOptions/>
    </template>
    <template #result-display>
      <DisplaySystem :card_list="bookmarks" :CardComponent="CardComponent" />
    </template>
  </ViewTemplate>
</template>

<script>
import axios from "axios";
import DisplaySystem from "@/components/display_system/index"
import PerformingOptions from "@/components/display_system/performing_options"
import Card from "@/components/display_system/cards/nonExplorerCard"
import ViewTemplate from "@/components/TheViewTemplate"

export default {
  name: "full-list",
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
  mounted () {
    // this.$store.dispatch("check_full_list")

    axios.get('http://127.0.0.1:5000/full_list')
          .then(response => {
            this.bookmarks = response.data
        })
  }
}
</script>
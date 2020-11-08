<template>
  <ViewTemplate>
    <template #control-panel>
      <div />
      <PerformingOptions/>
    </template>
    <template #result-display>
      <!-- <DisplaySystem :bookmarks="this.$store.state.sorted_all_bookmarks"/> -->
      <DisplaySystem :card_list="bookmarks" :click_card_head="clickCardHead"/>
    </template>
  </ViewTemplate>
</template>

<script>
import axios from "axios";
import DisplaySystem from "@/components/display_system/index"
import PerformingOptions from "@/components/display_system/performing_options"
import NonExplorerBase from "@/views/common_non_explorer_bookmarks_mixin"
import ViewTemplate from "@/components/TheViewTemplate"

export default {
  name: "full-list",
  components: {
    ViewTemplate,
    DisplaySystem,
    PerformingOptions
  },
  mixins: [NonExplorerBase],
  data () {
    return {
      bookmarks: []
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
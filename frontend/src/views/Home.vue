<template>
  <ViewTemplate>
    <template #control-panel>  
      <md-button class="md-dense md-primary" @click="fetch">Refetch</md-button>
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
  name: "randoms",
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
    sorting () {
      return this.$store.state.display['sorting']
    }
  },
  mounted(){
    this.fetch()
  },
  methods: {
    fetch() {
      this.bookmarks = []
      axios
        .get(`http://127.0.0.1:5000/bookmarks/${this.$store.state.display['sorting']}/${-1}`)
        .then(response => {
          this.bookmarks = response.data
        })
    }
  },
  watch: {
    sorting () {
      this.fetch()
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

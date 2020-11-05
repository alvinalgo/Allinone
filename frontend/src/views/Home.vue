<template>
  <div>
    <div class="flex-wrapper">  
      <md-button class="md-dense md-primary" @click="fetch">Refetch</md-button>
      <PerformingOptions/>
    </div>

    <DisplaySystem :card_list="bookmarks" :click_card_head="click_card_head"/>
  </div>
</template>

<script>
import axios from "axios";
import DisplaySystem from "@/components/display_system/index"
import PerformingOptions from "@/components/display_system/performing_options"
import non_explorer_base from "@/views/common_non_explorer_bookmarks_mixin"

export default {
  name: "randoms",
  components: {
    DisplaySystem,
    PerformingOptions
  },
  mixins: [non_explorer_base],
  data () {
    return {
      bookmarks: []
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

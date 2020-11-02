<template>
  <div class="view-wrapper">
    <h1>Full List</h1>
    <PagingSystem :bookmarks="this.$store.state.bookmark_bar"/>
  </div>
</template>

<script>
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
  mounted () {
    this.$store.dispatch("check_full_list")
  }
}
</script>

<style lang="scss" scoped>
.view-wrapper {
  width: 90%;
  margin: 0 auto;
}
</style>

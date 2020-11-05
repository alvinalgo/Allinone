<template>
  <div>
    <h1>Full List</h1>
    <DisplaySystem :bookmarks="this.$store.state.sorted_all_bookmarks"/>
  </div>
</template>

<script>
import DisplaySystem from "@/components/display_system/index"

export default {
  name: "folders",
  components: {
    DisplaySystem
  },
  mounted () {
    this.$store.dispatch("check_full_list")
  }
}
</script>
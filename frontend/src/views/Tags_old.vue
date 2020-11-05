<template>
  <div class="view-wrapper">
    {{this.$route.params.tag}}
    <DisplaySystem :bookmarks="this.$store.state.folders"/>
  </div>
</template>

<script>
import DisplaySystem from "@/components/display_system/index"

export default {
  name: "folders",
  components: {
    DisplaySystem
  },
  mounted() {
    this.$store.dispatch('check_folders')
  }
}
</script>

<style lang="scss">
.view-wrapper {
  width: 80%;
  margin: 0 auto;
}
</style>
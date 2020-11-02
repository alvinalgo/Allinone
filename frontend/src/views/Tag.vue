<template>
  <div class="view-wrapper">
    <h1>Tag</h1>
    {{this.$route.params.tag}}
    <Display :images="this.$store.state.folders"/>
  </div>
</template>

<script>
import store from "@/store"
import Display from "../components/fountain_display"

export default {
  name: "folders",
  components: {
    Display
  },
  mounted() {
    store.dispatch('check_folders')
  }
}
</script>

<style lang="scss">
.view-wrapper {
  width: 80%;
  margin: 0 auto;
}
</style>
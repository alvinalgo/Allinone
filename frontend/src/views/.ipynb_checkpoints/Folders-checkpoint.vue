<template>
  <div class="container">
    <h1>Folders</h1>
    <Fountain :images="this.$store.state.folders"/>
  </div>
</template>

<script>
import Fountain from "../components/fountain_display"

export default {
  name: "folders",
  components: {
    Fountain
  }
}
</script>

<style lang="scss" scoped>
.container {
  width: 80%;
  margin: 0 auto;
}
    
img {
  width: 100%;
  height: auto;
/*   border-radius: 12px; */
}
</style>

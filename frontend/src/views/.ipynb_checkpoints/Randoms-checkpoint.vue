<template>
  <div class="container">
      <h1>Randoms</h1>
      <Fountain :images="randoms"/>
  </div>
</template>

<script>
import axios from "axios";
import Fountain from "../components/fountain_display"

export default {
  name: "randoms",
  components: {
    Fountain
  },
  data: () => ({
    randoms: []
  }),
  mounted(){
    this.fetch_randoms()
  },
  methods: {
    fetch_randoms() {
      this.randoms = []
      axios
        .get('http://127.0.0.1:5000/randoms')
        .then(response => {
          this.randoms = response.data
        })
    }
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

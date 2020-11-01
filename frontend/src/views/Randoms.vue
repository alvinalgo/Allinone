<template>
  <div class="view-wrapper">
      
      <div class="align">
        <h1>Randoms</h1>
        <md-button class="md-dense md-primary" @click="fetch_randoms">Refetch</md-button>
      </div>
      <Display :images="randoms"/>
  </div>
</template>

<script>
import axios from "axios";
import Display from "../components/grid_display"

export default {
  name: "randoms",
  components: {
    Display
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
.view-wrapper {
  width: 80%;
  margin: 0 auto;
}

.align {
  display: flex;
  align-items: center;
}
</style>

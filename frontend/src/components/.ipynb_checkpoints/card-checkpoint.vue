<template>
  <md-card md-with-hover>
    <md-card-media md-ratio="16:9">
      <img :src="url">
    </md-card-media>
    <md-card-content v-if="name">
      {{name}}
    </md-card-content>
  </md-card>
</template>

<script>
export default {
  props: ['name', 'tags', 'url']
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

<template>
  <div class="grid-display-wrapper">
    <div v-for="(image, i) in images" :key="i"
      :class="get_class(i)"
      @mouseenter="focusing=i" @mouseleave="focusing=-1">

      <Card :width="200" :height="250" :image="image" :focusing="i === focusing"/>
    </div>
  </div>
</template>

<script>
import Card from "./event_card"

export default {
  name: "app",
  components: {
    Card
  },
  props: ['images'],
  data: () => ({
    focusing: -1
  }),
  methods : {
    get_class (i) {
      return {
        'card-wrapper': true,
        'focus': i === this.focusing,
        'non-focus': !(i === this.focusing)
      }
    }
  }
}
</script>

<style scoped>
.grid-display-wrapper {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: stretch;
}
</style>
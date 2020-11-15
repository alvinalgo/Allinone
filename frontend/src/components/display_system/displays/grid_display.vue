<template>
  <div class="grid-display-wrapper">
    <div v-for="(card_info, i) in card_list" :key="i"
      :class="get_class(i)"
      @mouseenter="focusing=i" @mouseleave="focusing=-1">

      <component :is="CardComponent" :card_info="card_info" :focusing="i === focusing" />
    </div>
  </div>
</template>

<script>
import passingCard from "@/mixins/passingCard.js"

export default {
  name: "grid-display",
  mixins: [passingCard],
  data: () => ({
    focusing: -1
  }),
  methods: {
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
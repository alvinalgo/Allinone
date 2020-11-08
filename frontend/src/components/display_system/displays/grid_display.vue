<template>
  <div class="grid-display-wrapper">
    <div v-for="(card_info, i) in card_list" :key="i"
      :class="get_class(i)"
      @mouseenter="focusing=i" @mouseleave="focusing=-1">

      <Card :width="200" :height="250" :card_info="card_info" :focusing="i === focusing" :click_card_head="click_card_head" />
    </div>
  </div>
</template>

<script>
import Card from "../cards/event_card"
import base from "./display_mixin.js"

export default {
  name: "grid-display",
  components: {
    Card
  },
  mixins: [base],
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
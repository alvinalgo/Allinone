<template>
  <div>
    <Display :card_list="card_list" :click_card_head="click_card_head"/>
  </div>
</template>

<script>
import Display from "./displays/fountain_display"
import base from "./system_mixin"

export default {
  name: "fountain-system",
  components: {
    Display
  },
  mixins: [base],
  mounted () {
    console.log(this.card_list)
  }
}
</script>
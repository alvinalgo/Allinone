<template>
  <component :is="displays[this.$store.state.display['display_style']]" :card_list="card_list" :click_card_head="click_card_head"/>
</template>

<script>
import grid_system from "@/components/display_system/grid_system"
import fountain_system from "@/components/display_system/fountain_system"
import base from "./system_mixin"

export default {
  name: "display-system",
  components: {
    grid_system,
    fountain_system
  },
  mixins: [base],
  data() {
    return {
      displays: {
        'grid_display': grid_system,
        'fountain_display': fountain_system
      }
    }
  }
}
</script>
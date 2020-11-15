<template>
  <component :is="displays[this.$store.state.display['display_style']]" :card_list="card_list" :CardComponent="CardComponent" />
</template>

<script>
import grid_system from "@/components/display_system/grid_system"
import fountain_system from "@/components/display_system/fountain_system"
import passingCard from "@/mixins/passingCard.js"

export default {
  name: "display-system",
  components: {
    grid_system,
    fountain_system
  },
  mixins: [passingCard],
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
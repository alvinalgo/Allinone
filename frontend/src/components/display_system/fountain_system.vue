<template>
  <div v-infinite-scroll="loadMore" infinite-scroll-disabled="cannotScroll" infinite-scroll-distance="100">
    <Display :card_list="getDisplayingSlice" :CardComponent="CardComponent" />
  </div>
</template>

<script>
import Display from "./displays/grid_display"
import passingCard from "@/mixins/passingCard.js"

export default {
  name: "fountain-system",
  components: {
    Display
  },
  mixins: [passingCard],
  data () {
    return {
      displayingEnd: this.$store.state.display.displayingSize
    }
  },
  mounted () {
    console.log(this.cannotScroll, this.displayingEnd, this.card_list.length)
    this.cannotScroll = false
  },
  computed: {
    getDisplayingSlice () {
      return this.card_list.slice(0, this.displayingEnd)
    },
    cannotScroll () {
      return this.displayingEnd >= this.card_list.length
    }
  },
  methods: {
    loadMore () {
      this.displayingEnd += this.$store.state.display.displayingSize
    }
  }
}
</script>
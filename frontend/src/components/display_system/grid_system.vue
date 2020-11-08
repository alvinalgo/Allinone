<template>
  <div>
    <div class="align">
      <md-button class="md-dense md-raised" :to="{params: {startIndex: valid_page(false)}}" replace>&lt;</md-button>
      <md-button class="md-dense md-raised" :to="{params: {startIndex: valid_page(true)}}" replace>&gt;</md-button>
      {{ startIndex }} - {{ startIndex + this.$store.state.display.displayingSize }}
    </div>
    <Display :card_list="get_displaying_slice()" :click_card_head="click_card_head"/>
  </div>
</template>

<script>
import Display from "./displays/grid_display"
import base from "./system_mixin"

export default {
  name: "grid-system",
  components: {
    Display
  },
  mixins: [base],
  computed: {
    startIndex(){
      var index = this.$route.params.startIndex
      return index ? parseInt(index) : 0
    },
  },
  methods: {
    get_displaying_slice () {
      return this.card_list.slice(this.startIndex, this.startIndex+this.$store.state.display.displayingSize)
    },
    valid_page (is_next_page) {
      if (is_next_page) {
        return this.startIndex+this.$store.state.display.displayingSize > this.card_list.length ?
          this.startIndex : this.startIndex+this.$store.state.display.displayingSize
      }
      else {
        return Math.max(this.startIndex-this.$store.state.display.displayingSize, 0)
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.align {    // 頁碼對齊
  display: flex;
  align-items: baseline;
}

.md-ripple {    // 換頁鍵
  margin: 10px 0px;
}
</style>
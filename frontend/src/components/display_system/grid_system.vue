<template>
  <div>
    <div class="align">
      <md-button class="md-dense md-raised" :to="{params: {start_index: valid_page(false)}}" replace>&lt;</md-button>
      <md-button class="md-dense md-raised" :to="{params: {start_index: valid_page(true)}}" replace>&gt;</md-button>
      {{ start_index }} - {{ start_index + 20 }}
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
    start_index(){
      var index = this.$route.params.start_index
      return index ? parseInt(index) : 0
    },
  },
  methods: {
    get_displaying_slice () {
      return this.card_list.slice(this.start_index, this.start_index + 20)
    },
    valid_page (is_next_page) {
      if (is_next_page) {
        return this.start_index+20 > this.card_list.length ?
          this.start_index : this.start_index+20
      }
      else {
        return Math.max(this.start_index-20, 0)
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
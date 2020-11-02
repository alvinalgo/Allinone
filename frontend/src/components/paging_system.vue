<template>
  <div>
    <div class="align">
      <md-button class="md-dense md-raised" :to="{name:this.$router.currentRoute.name, params: {start_index: valid_page(false)}}">&lt;</md-button>
      <md-button class="md-dense md-raised" :to="{name:this.$router.currentRoute.name, params: {start_index: valid_page(true)}}">&gt;</md-button>
      {{ start_index }} - {{ start_index + 20 }}
    </div>
    <Display :images="get_displaying_slice()"/>
  </div>
</template>

<script>
import Display from "../components/grid_display"

export default {
  name: "paging-system",
  components: {
    Display
  },
  props: ['bookmarks'],
  computed: {
    start_index(){
      var index = this.$route.params.start_index
      return index ? parseInt(index) : 0
    }
  },
  methods: {
    get_displaying_slice () {
      return this.bookmarks.slice(this.start_index, this.start_index + 20)
    },
    valid_page (is_next_page) {
      if (is_next_page) {
        return this.start_index+20 > this.bookmarks.length ?
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
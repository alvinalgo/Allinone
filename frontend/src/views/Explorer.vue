<template>
  <div class="view-wrapper">
    <h1>Explorer</h1>
    <div class="align">
      <md-button class="md-dense md-raised" :to="{name: 'explorer', params: {start_index: valid_page(false)}}">&lt;</md-button>
      <md-button class="md-dense md-raised" :to="{name: 'explorer', params: {start_index: valid_page(true)}}">&gt;</md-button>
      {{ start_index }} - {{ start_index + 20 }}
    </div>
    <Display :images="get_displaying_slice()"/>
  </div>
</template>

<script>
import Display from "../components/grid_display"

export default {
  name: "folders",
  components: {
    Display
  },
  computed: {
    start_index(){
      var index = this.$route.params.start_index
      return index ? index : 0
    }
  },
  methods: {
    get_displaying_slice () {
      return this.$store.state.bookmark_bar.slice(this.start_index, this.start_index + 20)
    },
    valid_page (is_next_page) {
      if (is_next_page) {
        return this.start_index+20 > this.$store.state.bookmark_bar.length ?
          this.start_index : this.start_index+20
      }
      else {
        return Math.max(this.start_index-20, 0)
      }
    }
  },
  mounted () {
    this.$store.dispatch("check_explorer")
  }
}
</script>

<style lang="scss" scoped>
.view-wrapper {
  width: 90%;
  margin: 0 auto;
}

.align {
  display: flex;
  align-items: baseline;
}

.md-ripple {
  margin: 10px 0px;
}
</style>
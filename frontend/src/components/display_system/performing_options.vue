<template>
  <div>
  
  <!-- vue material -->
  <!-- <div class="md-layout-item">
    <md-field>
      <label for="display">Display</label>
      <md-select v-model="Display" name="display" @change="update_display">
        <md-option value="grid_display">Grid</md-option>
        <md-option value="fountain_display">Fountain</md-option>
      </md-select>
    </md-field>
  </div> -->

  <!-- no vue-meterial -->
  <div class="flex-wrapper">
    <div class="option_div">
      <label for="display">Display</label> <br>
      <select v-model="display_style" name="display" @change="update_display">
        <option value="grid_display">Grid</option>
        <option value="fountain_display">Fountain</option>
      </select>
    </div>
    <div class="option_div">
      <label for="sorting">Sort By</label> <br>
      <select v-model="sorting" name="sorting" @change="update_sorting">
        <option value="recents">Recent</option>
        <option value="randoms">Random</option>
      </select>
    </div>
  </div>

  <!-- checking -->
  <!-- {{ Display }} <br>
  {{ this.$store.state.display }} -->
  </div>
</template>

<script>
export default {
  name: "folders",
  data () {
    return {
      display_style: this.$store.state.display['display_style'],
      sorting: this.$store.state.display['sorting']
    }
  },
  methods: {
    update_display () {
      this.$store.dispatch('update_display', this.display_style)
    },
    update_sorting () {
      this.$store.dispatch('update_sorting', this.sorting)
    },
  }
}
</script>

<style scoped>
.flex-wrapper {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}
</style>

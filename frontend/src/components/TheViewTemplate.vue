<template>
  <div>
    <div class="flex-wrapper sticky">
      <slot class="flex-wrapper sticky" name="control-panel">
        <PerformingOptions />
      </slot>
    </div>
    <div class="percent80">
      <slot name="result-display" />
    </div>
  </div>
</template>

<script>
import PerformingOptions from "@/components/display_system/performing_options"

export default {
  name: "view-template",
  components: {
    PerformingOptions
  }
}
</script>

<style lang="scss" scoped>
.flex-wrapper {
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-between;
  align-items: center;
}

.sticky {
  position: sticky;
  background-color: antiquewhite;
  top: 0;
  padding: 0 10%;
  z-index: 10;
}

.percent80 {
  position: relative;
  margin: auto;
  width: 80%;
}
</style>
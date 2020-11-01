<template>
  <div id="wrapper"> 
    <stack
      :column-min-width="300"
      :gutter-width="15"
      :gutter-height="15"
      monitor-images-loaded
    >
      <stack-item
        v-for="(image, i) in images" :key="i"
      >
        <div :class="i === focusing ? 'focus' : 'non-focus'"
          @mouseenter="focusing=i" @mouseleave="focusing=-1">
          <Card :width="250" :height="250" :image="image" :focusing="i === focusing"/>
        </div>
      </stack-item>
    </stack>
  </div>
</template>

<script>
import { Stack, StackItem } from "vue-stack-grid";
import Card from "./event_card"

export default {
  name: "app",
  components: {
    Stack,
    StackItem,
    Card
  },
  data: () => ({
    focusing: -1
  }),
  props: ['images'],
  computed: {
    is_focus (i) {
      return i === this.focusing ? "focus" : ""
    }
  }
}
</script>
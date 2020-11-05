<template>
  <div id="wrapper"> 
    <stack
      :column-min-width="300"
      :gutter-width="15"
      :gutter-height="15"
      monitor-images-loaded
    >
      <stack-item
        v-for="(card_info, i) in card_list" :key="i"
      >
        <div :class="i === focusing ? 'focus' : 'non-focus'"
          @mouseenter="focusing=i" @mouseleave="focusing=-1">
          <Card :width="250" :height="250" :card_info="card_info" :focusing="i === focusing" :click_card_head="click_card_head"/>
        </div>
      </stack-item>
    </stack>
  </div>
</template>

<script>
import { Stack, StackItem } from "vue-stack-grid";
import base from "./display_mixin.js"
import Card from "../cards/event_card"


export default {
  name: "app",
  components: {
    Stack,
    StackItem,
    Card
  },
  mixins: [base],
  computed: {
    is_focus (i) {
      return i === this.focusing ? "focus" : ""
    }
  }
}
</script>
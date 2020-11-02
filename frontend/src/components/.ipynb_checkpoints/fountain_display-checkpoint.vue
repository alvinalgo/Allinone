<template>
  <div id="wrapper"> 
      <stack
        :column-min-width="300"
        :gutter-width="15"
        :gutter-height="15"
        monitor-images-loaded
      >
        <stack-item
          v-for="(image, i) in images"
          :key="i"
        >
          <a :href="image.url">
            <Card :name="image.name" :url="get_image_url(image)" :tags="0"/>
          </a>
        </stack-item>
      </stack>    
  </div>
</template>

<script>
import { Stack, StackItem } from "vue-stack-grid";
import Card from "./card"

export default {
  name: "app",
  components: {
    Stack,
    StackItem,
    Card
  },
  props: ['images'],
  methods: {
    get_image_url(image){
      if (image.type == 'folder'){return 'http://127.0.0.1:5000/icon/folder.jpg'}
      else {return `http://127.0.0.1:5000/images/${image.guid}`}
    }
  }
}
</script>

<style>
    
.wrapper {
/*   position: relative; */
}
    
img {
  width: 100%;
  height: auto;
/*   border-radius: 12px; */
}
</style>

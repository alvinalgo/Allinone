<template>
  <div id="app">
    <div class="container">
        
      <stack
        :column-min-width="300"
        :gutter-width="15"
        :gutter-height="15"
        monitor-images-loaded
      >
        <stack-item
          v-for="(image, i) in images"
          :key="i"
          style="transition: transform 450ms"
        >
          <a :href="image.url">
            <Card :name="image.name" :url="get_image_url(image.guid)" :tags="0"/>
          </a>
        </stack-item>
      </stack>
        
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { Stack, StackItem } from "vue-stack-grid";
import Card from "./components/card"

export default {
  name: "app",
  components: {
    Stack,
    StackItem,
    Card
  },
  data: () => ({
    images: []
  }),
  mounted(){
    this.fetch_random()
  },
  methods: {
    fetch_random() {
      this.images = []
      axios
        .get('http://127.0.0.1:5000/metadata')
        .then(response => {
          this.images = response.data
        })
        .catch(() => {
          this.images = []
        })
    },
    get_image_url(guid){return `http://127.0.0.1:5000/images/${guid}`}
  }
};
</script>
<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
/*   color: #2c3e50; */
  margin-top: 100px;
}
    
.container {
  width: 80vw;
  margin: 0 auto;
}
    
img {
  width: 100%;
  height: auto;
/*   border-radius: 12px; */
}
</style>

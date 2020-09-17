<template>
  <div id="app">
    <div class="container">
      <div class="button-wrapper">
        <button class="btn" @click="searchUnsplash('Autumn')">Autumn</button>
        <button class="btn" @click="searchUnsplash('cliff')">Cliff</button>
        <button class="btn" @click="searchUnsplash('ocean')">Ocean</button>
      </div>
      <stack
              :column-min-width="300"
              :gutter-width="15"
              :gutter-height="15"
              monitor-images-loaded
      >
        <stack-item
                v-for="(image, i) in images"
                :key="i"
                style="transition: transform 300ms"
        >
          <img :src="image" :alt="image" />
        </stack-item>
      </stack>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { Stack, StackItem } from "vue-stack-grid";

export default {
  name: "app",
  components: {
    Stack,
    StackItem
  },
  data: () => ({
    images: []
  }),
  methods: {
    searchUnsplash() {
      this.images = [];
      axios
        .get('http://127.0.0.1:5000/metadata')
        .then(response => {
          this.images = response.data;
        })
        .catch(() => {
          this.images = [];
        });
    }
  }
};
</script>
<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.container {
  width: 80vw;
  margin: 0 auto;
}
.button-wrapper {
  display: flex;
  justify-content: center;
  margin-bottom: 25px;
}
.btn {
  font-size: 18px;
  background-color: #42b983;
  color: white;
  padding: 10px 20px;
}
.btn:not(:last-child) {
  margin-right: 10px;
}
img {
  width: 100%;
  height: auto;
  border-radius: 12px;
}
</style>

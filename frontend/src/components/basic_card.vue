<template>
  <a class="basic-card" :href="image.url" >
    <md-card md-with-hover :style="card_style">
      <md-card-media md-ratio="16:9">
        <img :src="image.img_url">
      </md-card-media>
      <md-card-content v-if="image.name" :style="name_style">
        {{ image.name }}
      </md-card-content>
      <div class="flex" v-if="focusing">
        <md-button class="md-dense md-primary" v-for="tag in image.keyword" :key="tag">{{tag}}</md-button>
      </div>
    </md-card>
  </a>
</template>

<script>
export default {
  props: ['image', 'focusing'],
  computed: {
    name_style () {
      return {
        overflow: this.focusing ? '' : 'hidden',
        textOverflow: 'ellipsis',
        whiteSpace: this.focusing ? '' : 'nowrap',
    }},
    card_style () {
      return {
        transform: this.focusing ? 'scale(1.2)' : ''
      }
    }
  }
}
</script>

<style scoped>
.flex {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-items: stretch;
}

.md-ripple {
  padding: 0px;
}
</style>
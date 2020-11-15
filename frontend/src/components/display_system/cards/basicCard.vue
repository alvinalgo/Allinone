<template>
  <div class="basic-card">
    <md-card md-with-hover :style="card_style">
      <a @click.prevent="click_card_head(card_info)">
        <md-card-media md-ratio="16:9">
          <img :src="card_info.img_url">
        </md-card-media>
        <md-card-content v-if="card_info.name" :style="title_style">
          {{ card_info.name }}
        </md-card-content>
      </a>
      <div class="flex" v-if="focusing">
        <md-button class="md-dense md-primary" v-for="tag in card_info.keyword" :key="tag" :to="{name:'Tags', params:{tag:tag, clusteringMethod:'word_tokenized'}}">{{tag}}</md-button>
      </div>
    </md-card>
  </div>
</template>

<script>
export default {
  props: ['card_info', 'focusing', 'click_card_head'],
  computed: {
    title_style () {
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
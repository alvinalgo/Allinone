<template>
  <div class="basic-card">
    <md-card md-with-hover :style="card_style">
      <a @click.prevent="click_card">
        <md-card-media md-ratio="16:9">
          <img :src="datum.img_url">
        </md-card-media>
        <md-card-content v-if="datum.name" :style="name_style">
          {{ datum.name }}
        </md-card-content>
      </a>
      <div class="flex" v-if="focusing">
        <md-button class="md-dense md-primary" v-for="tag in datum.keyword" :key="tag" :to="{name:'tag', params:{'tag':tag}}">{{tag}}</md-button>
      </div>
    </md-card>
  </div>
</template>

<script>
export default {
  props: ['datum', 'focusing'],
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
  },
  methods: {
    click_card() {
      if(this.datum['type'] == 'folder') {
        this.$store.dispatch('stack_the_folder', this.datum)
        this.$router.push({name:'explorer', params:{target_index:this.datum['id'], start_index:0}})
      }
      else {
        window.open(this.datum['url'], "_blank")
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
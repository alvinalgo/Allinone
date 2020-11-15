<template>
  <div id="cardWrapper" :style="wrapper_style">
    <Card :style="card_style" :card_info="modifyImageUrl(card_info)" :focusing="focusing" :click_card_head="clickCardHead"
      @contextmenu.native.prevent="rightClicked"/>
  </div>
</template>

<script>
import Card from "./basicCard"
import modifyImageUrl from "@/mixins/modifyImageUrl"

export default {
  props: ['card_info', 'focusing', 'width', 'height', 'margin', 'clickCardHead'],
  components: {
    Card
  },
  mixins: [modifyImageUrl],
  data () {
    return {
      wrapper_style: {
        margin: (this.margin?this.margin:10) + 'px',
      },
      card_style: {
        width: (this.width?this.width:200) + 'px',
        height: (this.height?this.height:200) + 'px',
      }
    }
  },
  methods: {
    rightClicked () {
      console.log(`right clicked on ${this.card_info.id}`)
      this.$store.dispatch('updateInfoId', this.card_info.id)
    }
  }
}
</script>
<template>
  <Card :card_info="card_info" :focusing="focusing" :clickCardHead="clickCardHead"/>
</template>

<script>
import Card from "./wrappedCard"

export default {
  props: ['card_info', 'focusing'],
  components: {
    Card
  },
  methods: {
    clickCardHead (bookmarks) {
      if(bookmarks['type'] == 'folder') {
        this.$store.dispatch('stack_the_folder', bookmarks)
        this.$router.push({params:{targetIndex:bookmarks['id'], startIndex:0}})
      }
      else {
        window.open(bookmarks['url'], "_blank")
      }
    }
  }
}
</script>
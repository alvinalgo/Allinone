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
    clickCardHead (bookmark) {
      if(bookmark['type'] == 'folder') {
        this.$router.push({name: 'Folders', params:{folderId: bookmark['id'], startIndex: '0'}})
      } else if(bookmark['type'] == 'tag') {
        this.$router.push({name: 'Tags', params:{tag: bookmark['name'], startIndex: '0'}})
      } else {
        window.open(bookmark['url'], "_blank")
      }
    },
  }
}
</script>
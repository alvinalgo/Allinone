export default {
  methods: {
    click_card_head (bookmarks) {
      if(bookmarks['type'] == 'folder') {
        this.$router.push({name: 'Folders', params:{folder_id: bookmarks['id'], start_index: '0'}})
      }
      else {
        window.open(bookmarks['url'], "_blank")
      }
    }
  }
}
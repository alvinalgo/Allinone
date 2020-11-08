export default {
  methods: {
    clickCardHead (bookmarks) {
      if(bookmarks['type'] == 'folder') {
        this.$router.push({name: 'Folders', params:{folderId: bookmarks['id'], startIndex: '0'}})
      }
      else {
        window.open(bookmarks['url'], "_blank")
      }
    }
  }
}
export default {
  methods: {
    modifyImageUrl (cardInfo) {
      var newCardInfo = cardInfo
      if (newCardInfo.type == 'folder'){newCardInfo.img_url = 'http://127.0.0.1:5000/icon/folder.jpg'}
      else if (newCardInfo.type == 'tag'){newCardInfo.img_url = 'http://127.0.0.1:5000/icon/tag.png'}
      else {newCardInfo.img_url =  `http://127.0.0.1:5000/images/${newCardInfo.guid}`}
      
      return newCardInfo
    }
  }
}
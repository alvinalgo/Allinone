<template>
  <div class="event-card" :style="wrapper_style">
    <Card :style="card_style" :card_info="modify_image_url" :focusing="focusing" :click_card_head="click_card_head"/>
  </div>
</template>

<script>
import Card from "./basic_card"

export default {
  props: ['card_info', 'focusing', 'width', 'height', 'click_card_head'],
  components: {
    Card
  },
  data () {
    return {
      wrapper_style: {
        width: (this.width?this.width:200) + 'px',
        height: (this.height?this.height:200) + 'px',
        display: 'flex'
      },
      card_style: {
        width: (this.width?this.width:200) + 'px',
        height: (this.height?this.height:200) + 'px',
      }
    }
  },
  computed: {
    modify_image_url () {
      var new_card_info = this.card_info
      if (new_card_info.type == 'folder'){new_card_info.img_url = 'http://127.0.0.1:5000/icon/folder.jpg'}
      else if (new_card_info.type == 'tag'){new_card_info.img_url = 'http://127.0.0.1:5000/icon/tag.jpg'}
      else {new_card_info.img_url =  `http://127.0.0.1:5000/images/${new_card_info.guid}`}
      
      return new_card_info
    }
  }
}
</script>
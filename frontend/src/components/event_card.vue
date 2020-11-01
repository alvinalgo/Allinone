<template>
  <div class="event-card" :style="wrapper_style">
    <Card :style="card_style" :image="modify_image" :focusing="focusing"/>
  </div>
</template>

<script>
import Card from "./basic_card"

export default {
  props: ['image', 'focusing', 'width', 'height'],
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
    modify_image () {
      var new_image = this.image
      if (new_image.type == 'folder'){new_image.img_url = 'http://127.0.0.1:5000/icon/folder.jpg'}
      else {new_image.img_url =  `http://127.0.0.1:5000/images/${new_image.guid}`}
      
      return new_image
    }
  }
}
</script>
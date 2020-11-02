<template>
  <div class="event-card" :style="wrapper_style">
    <Card :style="card_style" :datum="modify_image_url" :focusing="focusing"/>
  </div>
</template>

<script>
import Card from "./basic_card"

export default {
  props: ['datum', 'focusing', 'width', 'height'],
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
      var new_datum = this.datum
      if (new_datum.type == 'folder'){new_datum.img_url = 'http://127.0.0.1:5000/icon/folder.jpg'}
      else {new_datum.img_url =  `http://127.0.0.1:5000/images/${new_datum.guid}`}
      
      return new_datum
    }
  }
}
</script>
<template>
  <div v-if="slotProps.ready" class="scrollable">
    <img id="headingImg" :src="info.img_url">
    <div id="content">
      <h2>{{ info.name }}</h2>
      <span v-for="(path, i) in paths" :key="i">
        &gt;
        <a @click.prevent="redirect_page(path)">
          {{path.name}}
        </a>
      </span>
    </div>
  </div>
</template>

<script>
import modifyImageUrl from "@/mixins/modifyImageUrl"

export default {
  mixins: [modifyImageUrl],
  props: ['slotProps'],
  computed: {
    info () { return this.modifyImageUrl(this.slotProps.info)},
    paths () { return this.slotProps.paths}
  },
  methods: {
    exit () {
      this.$store.dispatch('updateInfoId', false)
    },
    redirect_page (bookmark) {
      this.exit()
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

<style scoped>
#headingImg {
  width: 100%;
}

#content {
  width: 90%;
  margin: auto;
}
</style>
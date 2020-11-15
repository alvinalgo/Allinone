<template>
  <div :class="{wholeArea:!(this.$store.state.displayingInfoId), top:this.$store.state.displayingInfoId}" @click.self="exit" @contextmenu.self.prevent="exit">
    <div class="infoCardPositioning">
      <div :class="{infoOn: this.$store.state.displayingInfoId, infoCard: true}">
        <slot name="infoContent" :info="info" :paths="paths" :ready="ready">
          default slot
          {{ info }}
        </slot>
        <div id="blank" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: "view-template",
  data () {
    return {
      info: '',
      readyToRender: {
        info: false,
        paths: false
      },
      paths: []
    }
  },
  computed: {
    displayingInfoId () {
      return this.$store.state.displayingInfoId
    },
    ready () {
      return this.readyToRender['info'] && this.readyToRender['paths']
    }
  },
  methods: {
    fetchInfo () {
      this.readyToRender['info'] = false
      this.readyToRender['paths'] = false

      axios.get(`http://127.0.0.1:5000/info/${this.$store.state.displayingInfoId}`)
      .then(response => {
        this.info = response.data
        this.readyToRender['info'] = true
      })
      axios.get(`http://127.0.0.1:5000/get_parents_and_self/${this.$store.state.displayingInfoId}`)
      .then(response => {
        this.paths = response.data
        this.readyToRender['paths'] = true
      })
    },
    exit () {
      this.$store.dispatch('updateInfoId', false)
    }
  },
  watch: {
    displayingInfoId () {
      if (this.displayingInfoId != false) {
        this.fetchInfo()
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.top {
  height: 100vh;
  width: 100vw;
  z-index: 3;
  transition: z-index 0ms 100ms;
}

.wholeArea {
  z-index: -1;
  transition: z-index 0ms 200ms;
}

.infoCardPositioning {
  position: absolute;
  top: 5vh;
  right: 50px;
  height: 90%;
  width: 800px;
}

.infoCard {
  position: absolute;
  height: 100%;
  width: 75%;
  color: #ffffff;
  background-color: #202124ff;
  overflow: scroll;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  opacity: 0;
  transform: translateX(25%);
  transition: transform 200ms 100ms ease-out, width 200ms 100ms ease-out, opacity 200ms ease-out;

  &:hover {
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
  }

  &::-webkit-scrollbar {
    display: none;
  }
}

#blank {
  height: 50px;
}

.infoOn {
  width: 100%;
  opacity: 1;
  transform: none;
  transition: transform 200ms ease-out, width 200ms ease-out, opacity 200ms 100ms ease-out;;
}
</style>
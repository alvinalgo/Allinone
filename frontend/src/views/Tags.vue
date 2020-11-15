<template>
  <ViewTemplate>
    <template v-slot:control-panel>
      <h2>{{ name }}</h2>
      <div>
        <ul>
          <li v-for="method in clusteringMethodList" :key="method"><a @click.prevent="clickClusteringMethod(method)">{{ method }}</a></li>
        </ul>
      </div>
      <PerformingOptions/>
    </template>
    <template v-slot:result-display>
      <DisplaySystem :card_list="card_list" :CardComponent="CardComponent" />
    </template>
  </ViewTemplate>
</template>

<script>
import axios from "axios"
import DisplaySystem from "@/components/display_system/index"
import Card from "@/components/display_system/cards/nonExplorerCard"
import PerformingOptions from "@/components/display_system/performing_options"
import ViewTemplate from "@/components/TheViewTemplate"

export default {
  name: "folders",
  components: {
    ViewTemplate,
    DisplaySystem,
    PerformingOptions
  },
  data () {
    return {
      card_list: [],
      clusteringMethod: 'word_tokenized',
      clusteringMethodList: ['word_tokenized', 'web_domain'],
      name: '',
      CardComponent: Card,
    }
  },
  mounted() {
    if (this.$route.params.tag === '-1') {
      this.fetchAClusterMethod()
    } else {
      axios.get(`http://127.0.0.1:5000/query_a_tag/${this.$route.params.clusteringMethod}/${this.$route.params.tag}`)
        .then(response => {
          this.name = response.data['name']
          this.card_list = response.data['children']
      })
    }
  },
  methods: {
    fetchAClusterMethod () {
      axios.get(`http://127.0.0.1:5000/tags/${this.$route.params.clusteringMethod}`)
        .then(response => {
          this.name = 'All tags'
          this.card_list = response.data
      })
    },
    clickClusteringMethod (method) {
      this.$router.replace({name:'Tags', params:{tag:'-1', clusteringMethod:method}}).catch(() => {})
    },
  },
  watch: {
    clusteringMethod () {
      this.fetchAClusterMethod()
    }
  }
}
</script>

<style lang="scss" scoped>
ul {
  display: flex;
  justify-content: space-between;
  padding: 0px;
  text-align: center;
    
  li {
    list-style: none;
    padding: 0px 30px;
  }
}
</style>
<template>
  <div id="app">
    <div class="header">
      <div class="title"><h1>{{ this.$router.currentRoute.name }}</h1></div>
      <TheNavigator id="nav"/>
      <img src="@/assets/search_icon.jpg" width="40px" height="40px">
    </div>
    <router-view id="router-view-wrapper" :key="$route.path" />
    <InfoWindow class="coverWhole">
      <template #infoContent="slotProps">
        <InfoWindowContent :slotProps="slotProps" />
      </template>
    </InfoWindow>
  </div>
</template>

<script>
import TheNavigator from "@/components/TheNavigator"
import InfoWindow from "@/components/infoWindowTemplate"
import InfoWindowContent from "@/components/infoWindowContent"
    
export default {
  name: "app",
  components: {
    TheNavigator,
    InfoWindow,
    InfoWindowContent
  }
}
</script>

<style lang="scss" scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  background: #ffffff;
}

.coverWhole {
  position: fixed;
  top: 0;
  right: 0;
  height: 100vh;
  width: 100vw;
}

.title {
  width: 150px;
  color: #ffffff;
}

.header {
  background: #48b599;
//     linear-gradient(339deg, rgba(5,195,132,1) 0%, rgba(29,223,169,1) 100%);
  position: absolute;
  top: 0;
  height: 70px;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0px 50px;
}

#router-view-wrapper {
  position: relative;
  margin: auto;
  top: 70px;
}
    
h1 {
  padding: 10px;
}
</style>
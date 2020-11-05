<template>
  <div id="app">
    <div class="header">
      <div class="title"><h1>{{ this.$router.currentRoute.name }}</h1></div>
      <TheNavigator id="nav"/>
      <img src="@/assets/search_icon.jpg" width="40px" height="40px">
    </div>
    <div id="router-view-wrapper"><router-view :key="$route.path"/></div>
  </div>
</template>

<script>
import TheNavigator from "@/components/TheNavigator"
    
export default {
  name: "app",
  components: {
    TheNavigator
  }
}
</script>

<style lang="scss" scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.title {
  width: 150px;
  color: #ffffff;
}

.header {
  background: #48b599;
//     linear-gradient(339deg, rgba(5,195,132,1) 0%, rgba(29,223,169,1) 100%);
  position: sticky;
  top: 0;
  z-index: 100;
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
  width: 80%;
}
    
h1 {
  padding: 10px;
}
</style>
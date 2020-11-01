<template>
  <div id="app">
    <TheNavigator id="nav"/>
    <div id="router-view-wrapper"><router-view/></div>
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

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

#nav {
  background: #BBE1C3;
//     linear-gradient(339deg, rgba(5,195,132,1) 0%, rgba(29,223,169,1) 100%);
  position: fixed;
  height: 100vh;
  width: 10vw;
  padding: 0px;
}
    
#router-view-wrapper {
  position: absolute;
  top: 0px;
  left: 10vw;
  width: 90vw;
}
    
h1 {
  padding: 10px;
}
</style>
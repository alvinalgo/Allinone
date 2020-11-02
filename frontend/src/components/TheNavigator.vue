<template>
<nav>
<!--       <md-app-drawer :md-active.sync="panel" >
          <md-toolbar class="md-transparent" md-elevation="2">
            Navigation
          </md-toolbar> 
          <md-list> 
                <md-list-item> 
                <md-icon>aa</md-icon> 
                <span class="md-list-item-text"><router-link to="/">Home</router-link></span> 
                </md-list-item> 
                <md-list-item> 
                <md-icon>aaa</md-icon> 
            <span class="md-list-item-text"><router-link to="/">Home</router-link></span> 
          </md-list-item>
        </md-list>
      </md-app-drawer> -->
      
  <ul>
    <li><router-link :to="{name:'home'}">Home</router-link></li>
    <li><router-link :to="{name:'folders'}">Folders</router-link></li>
    <li><router-link :to="{name:'full_list', params:{'start_index': 0}}">Full List</router-link></li>
    <li><router-link :to="{name:'explorer', params:{
      'start_index': 0, 
      'target_index': this.$store.state.folder_stack.length ?
        this.$store.state.folder_stack.slice(-1)[0]['id'] : '-1'}
      }">Explorer</router-link></li>
  </ul>
</nav>
</template>

<script>
export default {
    name: 'TheNavigator'
}
</script>

<style lang="scss" scoped>
nav {
  display: flex;
  justify-content: center;
  
  ul {
    padding: 0px;
    text-align: center;
      
    li {
      list-style: none;
      padding: 10px 0px;
    }
  }
    
  a {
    text-decoration: none;
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
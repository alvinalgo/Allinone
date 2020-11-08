<template>
<div>
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
      <li><router-link :to="{name:'Home'}">Home</router-link></li>
      <li><router-link :to="{name:'Folders', params:{folderId: '-1'}}">Folders</router-link></li>
      <li><router-link :to="{name:'Full List', params:{'startIndex': 0}}">Full List</router-link></li>
      <li><router-link :to="{name:'Tags', params:{tag:'-1'}}">Tags</router-link></li>
      <!-- <li><router-link :to="{name:'Folders', params:{folder_id:'1891'}}">iinumbers</router-link></li> -->
      <li><router-link :to="{name:'Explorer', params: explorerParams}">Explorer</router-link></li>
    </ul>
  </nav>
</div>
</template>

<script>
export default {
  name: 'TheNavigator',
  computed: {
    explorerParams () {
      var targetIndex = this.$store.state.folder_stack.length ? this.$store.state.folder_stack.slice(-1)[0]['id'] : '-1'
      return {'startIndex': 0, 'targetIndex': targetIndex}
    }
  }
}
</script>

<style lang="scss" scoped>
nav {
  
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
    
  a {
    &:link, &:visited, &:hover, &:active {
      color: #ffffff;
      transition: none;
    }

    &.router-link-active {
      // font-weight: bold;
      // color: #ffffff;
    }

    &.router-link-exact-active {
      // font-weight: bold;
      // color: #0062d1;
    }
  }
}
</style>
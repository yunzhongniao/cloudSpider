<template>
  <a-layout id="components-layout-demo-top" class="layout">
    <a-layout-header>
      <div class="logo" />
      <a-menu
        theme="dark"
        mode="horizontal"
        :defaultSelectedKeys="['1']"
        :style="{ lineHeight: '64px' }"

      >
        <a-menu-item key="1"><router-link to="/">Home</router-link></a-menu-item>
        <a-menu-item key="2"><router-link to="/books">Books</router-link></a-menu-item>
        <a-menu-item key="3"><router-link to="/spiders">Spiders</router-link></a-menu-item>
        <a-menu-item key="4"><router-link to="/contacts">contacts</router-link></a-menu-item>
      </a-menu>
    </a-layout-header>
    <a-layout-content style="padding: 0 50px">
      <div :style="{ background: '#fff', padding: '24px', minHeight: '280px' }">
        <router-view></router-view>
      </div>
    </a-layout-content>
    <a-layout-footer style="text-align: center">
      Ant Design ©2018 Created by Ant UED
    </a-layout-footer>
  </a-layout>
</template>

<script>
import SpiderInstanceList from './SpiderInstanceList'

export default {
  name: 'Index',
  components: {SpiderInstanceList},
  data () {
    return {
    }
  },
  methods: {

  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#components-layout-demo-top .logo {
  width: 120px;
  height: 31px;
  background: rgba(255,255,255,.2);
  margin: 16px 24px 16px 0;
  float: left;
}
</style>

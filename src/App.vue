<template>
  <div>
    <!-- <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> -->
  </div>
  <router-view/>
</template>

<script>

import Header from '@/components/Header.vue'

export default {
    components:{
      Header
    }
}
</script>

<style>
  *,html{
    margin:0;
    padding:0;
  }
  body{
         background:#F5F5F5;
    }
</style>

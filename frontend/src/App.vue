<template>
  <div>
    <!-- <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> -->
  </div>
  <router-view/>
</template>

<script>

export default {
    components:{
      
    },
    mounted(){
      if(localStorage.getItem('logged') != 'true'){
        this.$router.push('/authication')
      }
    }
}
</script>

<style>
  *,html{
    margin:0;
    padding:0;
    /* max-width: 100%; */
    /* overflow-x: hidden; */
  }
  body{
         background:#F5F5F5;
         max-width: 100%;
         overflow-x: hidden;
         font-family: 'TT-Moscow';
    }
    @font-face {
        font-family: "TT-Moscow";
        src: local("TT-Moscow"),
        url(./fonts/TT-Moscow/TT_Moscow_Economy_Regular.ttf) format("truetype");
    }
</style>

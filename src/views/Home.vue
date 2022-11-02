<template>
  <div class="row" style="">
    <Header/>
    <div class="col-sm-2">
        <Menu />
    </div>
    <div style="background:#F5F5F5;" class="col-sm p-3">
        <p class="h2">
          Рекомендации
        </p>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Menu from '@/components/Menu.vue'
import Header from '@/components/Header.vue'

export default {
  name: 'Home',
  components: {
    Menu,Header
  }
}
</script>

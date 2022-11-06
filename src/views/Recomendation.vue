<template>
  <div class="row" style="">
    <!-- <Header /> -->
    <div class="col-sm-3">
        <Menu />
    </div>
    <div style="background:#F5F5F5;" class="col-sm-9 p-3">
        <p class="h2">
          Рекомендации
        </p>
        <div class="row mt-5 p-2">
            <div class="col-sm-3 p-2 rounded border" v-on:click="im_click" :class="im ? 'active' : 'non-acitve'" style="cursor:pointer">
                <p>Импорт</p>
            </div>
            <div class="col-sm-3 p-2 rounded border" v-on:click="ex_click" :class="ex ? 'active' : 'non-acitve'" style="margin-left:5%;cursor:pointer">
                <p>Экспорт</p>
            </div>
        </div>
        <div v-if="downloaded">
          <div v-for="(rec,key) in recs" :key="key" class="rounded p-2 mt-3" style="background:white;width:50%">
            <p :class="rec.clicked ? '' : 'text-truncate'">{{rec.name}}</p>
            <div class="row" style="width:45%;margin-left:5%">
              <p class="col-sm badge text-wrap p-2" style="background:#9EA7AF">{{rec.product_code}}</p>
              <p v-on:click="()=>rec.clicked=!rec.clicked" class="col-sm badge text-wrap p-2" style="background:#3E445B;margin-left:5%;cursor:pointer">Показать больше </p>
            </div>
          </div>
        </div>

        <div v-if="!downloaded" class="loader"></div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import Menu from '@/components/Menu.vue'
import Header from '@/components/Header.vue'


export default {
  name: 'Recomendation',
  components: {
    Menu,Header
  },
  data(){
    return{
      im: true,ex:false,dir:"IM",
      recs: [],
      downloaded: false,
    }
  },
  methods:{
    im_click(){
        this.im = true;
        this.ex = false;
        this.dir = "IM";
    
    },
    ex_click(){
        this.im = false;
        this.ex = true;
        this.dir = "EX";

    },
    getRecs(){
      axios.get('https://vl0i36.deta.dev/recommendations')
        .then(res=>{
          console.log(res.data);
          for(let i=0;i<4;i++){
            this.recs.push(res.data.stats[i]);
            this.recs[i]['clicked'] = false;
            this.downloaded = true;
          }
        })
        .catch(e=>{
          console.log(e);
        })
    }
  },
  mounted(){
    this.getRecs();
  },
}
</script>

<style scoped>
    .active{
        background:#1A8BCB;
        color:white;
        border-color:#1A8BCB
    }
    .non-acitve{
        background:white
    }
       .loader {
    border: 16px solid #f3f3f3; /* Light grey */
    border-top: 16px solid #3498db; /* Blue */
    border-radius: 50%;
    width: 120px;
    height: 120px;
    animation: spin 2s linear infinite;
    }

    @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
    }
</style>
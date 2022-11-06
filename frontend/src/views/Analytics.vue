<template>
  <div class="row" style="">
    <!-- <Header /> -->
    <div class="col-sm-3">
        <Menu @data="handleData($event)" />
    </div>
    <div style="background:#F5F5F5;" class="col-sm p-3">
        <p class="h2">
          Аналитика
        </p>

        <div class="row mt-5 p-2" style="width:50%">
            <div class="col-sm-3 p-2 rounded border" v-on:click="im_click" :class="im ? 'active' : 'non-acitve'" style="cursor:pointer">
                <p>Импорт</p>
            </div>
            <div class="col-sm-3 p-2 rounded border" v-on:click="ex_click" :class="ex ? 'active' : 'non-acitve'" style="margin-left:5%;cursor:pointer">
                <p>Экспорт</p>
            </div>
        </div>

        <div class="mt-3 rounded p-2" style="background:white;width:fit-content">
          <VueApexCharts v-if="download" type="line" width="650" :options="chartOptions" :series="series"></VueApexCharts>
          <div class="p-5" v-if="!gettedD">
            <p class="h2">Вы не ввели данные.</p>
          </div>
          <div v-if="gettedD & !download" class="loader"></div>
          <!-- {{[this.startM, this.endM, this.product, this.dir]}} -->
        </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import Menu from '@/components/Menu.vue'
import VueApexCharts from 'vue3-apexcharts'

export default {
  name: 'Recomendation',
  components: {
    Menu, VueApexCharts
  },
  methods:{
    handleData(e){
        [this.startM,this.endM,this.product] = e;
        this.gettedD = true;
        this.getData();
        
    },
    im_click(){
        this.im = true;
        this.ex = false;
        this.dir = "IM";
        if(this.download){

            // this.chartOptions['xaxis']['categories'] = [''];
            // this.series[0]['data'] = [''];
            this.getData();
        }
    },
    ex_click(){
        this.im = false;
        this.ex = true;
        this.dir = "EX";
        if(this.download){
            // this.chartOptions['xaxis']['categories'] = [''];
            // this.series[0]['data'] = [''];
            this.getData();
        }
    },
     getData(){
        const dataParams = {
            product: this.product,// 8515110000
            direction: this.dir,
            start: this.startM+'-2021',
            end: this.endM+'-2021'
        }
         axios.post("https://vl0i36.deta.dev/analysis/filter?",null,{params:dataParams,headers: {"Content-Type": "application/json"  }})
            .then(res => {
                // console.log(res.data.stats);
                // this.chartOptions['xaxis']['categories'] = [res.data.stats[0].operation_date];
                this.cats = [res.data.stats[0].operation_date];
                this.series[0]['data'] = [(Math.round(((res.data.stats[0].avg_cost) + Number.EPSILON) * 100) / 100)];
                for(let i=1;i<res.data.stats.length;i++){
                    this.series[0]['data'].push(Math.round(((res.data.stats[i].avg_cost) + Number.EPSILON) * 100) / 100);
                    // this.chartOptions['xaxis']['categories'].push(res.data.stats[i].operation_date);
                    this.cats.push(res.data.stats[i].operation_date);
                }
                this.series[0]['name'] = res.data.stats[0].name.slice(0,10) + '...';
                this.download = true;
                this.chartOptions['xaxis']['categories'] = this.cats;
                // console.log(this.chartOptions['xaxis']['categories'])
                // console.log(this.series[0]['data'])
            })  
            .catch(e => {
                console.log(e);
            })
    }
  },
  mounted(){
    // this.getData();
  },
  data(){
    return{
        im: true,ex:false, dir:'IM',product:'',startM:'',endM:'',download:false,gettedD:false,cats:[],
     series: [{
              name: '',
              data: ['']
          }],
      chartOptions: {
            colors:['#47FF8D'],
            chart: {
              height: 350,
              type: 'line',
              zoom: {
                enabled: false
              }
            },
            dataLabels: {
              enabled: false
            },
            stroke: {
                
              curve: 'straight'
            },
            // title: {
            //   text: 'Product Trends by Month',
            //   align: 'center'
            // },
            
            grid: {
              row: {
                colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
                opacity: 0.5
              },
            },
            xaxis: {
              categories: [''],
            }
      }
    }
  }
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

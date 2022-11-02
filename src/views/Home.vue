<template>
  <div class="row" style="">
    <!-- <Header /> -->
    <div class="col-sm-2">
        <Menu />
    </div>
    <div style="background:#F5F5F5;" class="col-sm p-3">
        <p class="h2">
          Рекомендации
        </p>
        <div class="mt-5 rounded p-2" style="background:white;width:fit-content">
          <VueApexCharts type="line" width="450" :options="chartOptions" :series="series"></VueApexCharts>
        </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Menu from '@/components/Menu.vue'
import Header from '@/components/Header.vue'
import VueApexCharts from 'vue3-apexcharts'

export default {
  name: 'Home',
  components: {
    Menu,Header, VueApexCharts
  },
  data(){
    return{
     series: [{
              name: "Компьютеры",
              data: [10, 41, 35, 51, 49, 62, 69, 91, 148]
          }],
      chartOptions: {
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
            title: {
              text: 'Product Trends by Month',
              align: 'center'
            },
            
            grid: {
              row: {
                colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
                opacity: 0.5
              },
            },
            xaxis: {
              categories: ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен'],
            }
      }
    }
  }
}
</script>

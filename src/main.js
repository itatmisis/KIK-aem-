import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VueApexCharts from "vue3-apexcharts";

const Vue = createApp(App);

Vue.use(router).mount('#app');
Vue.use(VueApexCharts);
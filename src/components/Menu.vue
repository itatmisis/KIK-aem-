<template>
        <div class="cont position-relative">
            <div class="mt-3">
                <img src="../assets/logo.svg" alt="">
            </div>
            <div class="mt-5">
                <div class="row" v-on:click="() => this.$router.push('/')">
                    <img height="25" src="../assets/menuIcon.svg" alt="" class="col-sm-2">
                    <p class="col-sm" style="cursor:pointer">Статистика</p>
                </div>
                <div class="row">
                    <img height="25" src="../assets/menuIcon.svg" alt="" class="col-sm-2">
                    <p class="col-sm">Аналитика</p>
                </div>
                <div class="row">
                    <img height="25" src="../assets/menuIcon.svg" alt="" class="col-sm-2">
                    <p class="col-sm">Рекомендации</p>
                </div>
                <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-1 border-bottom"></div>

                <div class="row" v-on:click="goToProfile">
                    <img height="25" src="../assets/menuIcon.svg" alt="" class="col-sm-2">
                    <p class="col-sm" style="cursor:pointer">Личный кабинет</p>
                </div>

                <div class="row sticky-bottom position-absolute bottom-0" v-on:click="()=>this.$router.push('/authication')">
                    <img height="30" src="../assets/menuIcon.svg" alt="" class="col-sm-2">
                    <p class="col-sm" style="cursor:pointer">Выход</p>
                </div>
            </div>
        </div>
</template>

<script>
import Header from '@/components/Header.vue'

export default {
    components:{
        Header
    },
    methods:{
        goToProfile(){
            this.$router.push('/profile')
        }
    }
}
</script>

<style scoped>
    .cont{
        padding:5%;
        height:100vh;
        background: white;
    }
</style>
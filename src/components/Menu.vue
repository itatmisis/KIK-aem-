<template>
        <div class="cont">
            <div class="mt-5">
                <div class="row">
                    <img height="25" src="../assets/menuIcon.svg" alt="" class="col-sm-2">
                    <p class="col-sm">Статистика</p>
                </div>
                <div class="row">
                    <img height="25" src="../assets/menuIcon.svg" alt="" class="col-sm-2">
                    <p class="col-sm">Аналитика</p>
                </div>
                <div class="row">
                    <img height="25" src="../assets/menuIcon.svg" alt="" class="col-sm-2">
                    <p class="col-sm">Рекомендации</p>
                </div>

                <div class="row sticky-bottom" style="margin-top:25rem">
                    <img height="25" src="../assets/menuIcon.svg" alt="" class="col-sm-2">
                    <p class="col-sm">Выход</p>
                </div>
            </div>
        </div>
</template>

<script>
import Header from '@/components/Header.vue'

export default {
    components:{
        Header
    }
}
</script>

<style scoped>
    .cont{
        padding:5%;
        height: 100%;
        background: white;
    }
</style>
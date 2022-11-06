<template>
        <div class="cont position-relative">
            <div class="mt-3">
                <img src="../assets/logo.svg" alt="">
            </div>
            <div class="mt-5">
                <div class="row" v-on:click="() => this.$router.push('/')">
                    <img style="height:10%;width:auto" src="../assets/anal_icon.svg" alt="" class="col-sm-3">
                    <p class="col-sm" style="cursor:pointer">Аналитика</p>
                    <img :height="touched ? 10 : 15" style="cursor:pointer" v-on:click="() => this.touched = !this.touched" :src="touched ? arr_d : arr_r" class="mt-2 col-sm" data-bs-toggle="collapse" href="#collapseExample" />
                </div>
                <div class="collapse mb-2" id="collapseExample">
                    <div class="row">
                        <p class="text-muted">Месяц</p>
                        <div class="col-sm-6 row">
                            <p class="col-sm-2">от</p>
                            <input v-model="startM" type="number" min="1" max="12" class="col-sm-2 form-control month_form"/>
                        </div>
                        <div class="col-sm-6 row">
                            <p class="col-sm-2">до</p>
                            <input v-model="endM" type="number" min="1" max="12" class="col-sm-2 form-control month_form"/>
                        </div>
                    </div>

                    <div class="mt-2">
                        <p class="text-muted">Код товара</p>
                        <div class="row">
                            <input v-model="code" class="col-sm-6 form-control border-end-0" style="margin-left:10%;width:60%" type="number"/>
                            <a v-on:click="sendData" class="btn col-sm-2" style="color:white;background:#3E445B"><img src="@/assets/arrow_btn.svg"/></a>
                        </div>
                    </div>
                    <div v-if='err'>
                        <p style="color:red;font-size:0.9rem">Ошибка ввода</p>
                    </div>
                </div>
                <div class="row" v-on:click="() => this.$router.push('/recomendation')">
                    <img style="height:10%;width:auto" src="../assets/rec_icon.svg" alt="" class="col-sm-3">
                    <p class="col-sm" style="cursor:pointer">Рекомендации</p>
                </div>
                <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-1 border-bottom"></div>

                <div class="row" v-on:click="goToProfile">
                    <img style="height:10%;width:auto" src="../assets/profile_icon.svg" alt="" class="col-sm-3">
                    <p class="col-sm" style="cursor:pointer">Личный кабинет</p>
                </div>

                <div class="row sticky-bottom position-absolute bottom-0" v-on:click="getOut">
                    <img style="height:5%;width:40%" src="../assets/logout_.svg" alt="" class="col-sm-2">
                    <p class="col-sm-6 text-muted" style="cursor:pointer">Выход</p>
                </div>
            </div>
        </div>
</template>

<script>
import Header from '@/components/Header.vue'

export default {
    data(){
        return{
            arr_d: require('@/assets/arrow_down.svg'),
            arr_r: require('@/assets/arrow_right.svg'),
            touched: false,
            startM: '',
            endM: '',
            code:'',
            err: false
        }
    },
    components:{
        Header
    },
    methods:{
        goToProfile(){
            this.$router.push('/profile')
        },
        getOut(){
            localStorage.clear();
            this.$router.push('/authication');
        },
        sendData(){
            if(this.startM >= this.endM || (this.startM == '' || this.endM == '' || this.code == '')){
                this.err = true;
                this.startM = '';
                this.endM = '';

            }else{
                this.err = false;
                if(this.startM.toString().length == 1){
                    this.startM = '0'+this.startM.toString()
                }
                if(this.endM.toString().length == 1){
                    this.endM = '0'+this.endM.toString();
                }
                this.$emit('data',[this.startM.toString(),this.endM.toString(),this.code.toString()])
            }
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
    .month_form{
        margin-left:13%;
        width:60%;
        height:80%;
        font-size:85%
    }
</style>
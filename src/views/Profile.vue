<template>
    <div class="row position-relative" style="">
        <!-- <Header /> -->
        <div class="col-sm-3">
            <Menu />
        </div>
        <div class="col-sm p-3">
            <div class="position-absolute top-50 start-50 translate-middle">
                <div class="p-5 rounded" style="background:white;width:25rem">
                    <div class="row">
                        <img class="circle col-sm-3" src="../assets/ava2.svg" alt="">
                        <div class="col-sm">
                            <p class="h5"> {{name}} </p>
                            <p style="margin-top:-0.5rem" class="text-muted"> {{jobTitle}} </p>
                        </div>
                    </div>

                    <div class="row mt-3">
                        <div class="col-sm">
                            <p><strong>Пароль: ******</strong></p>
                        </div>
                        <div class="col-sm-4">
                            <a class="btn" style="color:white;background:#444A60">Поменять</a>
                        </div>
                    </div>

                    <div class="row mt-3">
                        <div class="col-sm">
                            <p><strong>
                            Телефон:<br> +79******05
                            </strong></p>
                        </div>
                        <div class="col-sm-4">
                            <a class="btn" style="color:white;background:#444A60">Поменять</a>
                        </div>
                    </div>

                    <div class="row mt-3">
                        <div class="col-sm">
                            <p><strong>
                            Email:<br> so****@gmail.com
                            </strong></p>
                        </div>
                        <div class="col-sm-4">
                            <a class="btn" style="color:white;background:#444A60">Поменять</a>
                        </div>
                    </div>
                    
                </div>
                <div v-if="is_super==='true'" class="p-3 rounded text-center mt-3" style="background:white;width:25rem">
                    <a class="btn" style="color:white;background:#444A60" v-on:click="generateAuth">Сгенерировать логин и пароль</a>
                    <div v-if="login!=''" class="mt-2">
                        <p>Логин: {{login}}</p>
                    </div>
                    <div v-if="password!=''">
                        <p>Пароль: {{password}}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import Menu from '@/components/Menu.vue'

export default {
    components:{
        Menu
    },
    data(){
        return{
            name: 'Аркадий Паровозов',
            jobTitle: 'Сотрудник',
            is_super: 'false',
            login: '',
            password:''
        }
    },
    methods:{
        isSuper(){
            this.is_super = localStorage.getItem('super');
            if(this.is_super == 'true'){
                this.name = 'Иванов Иван';
                this.jobTitle = 'Админ';
            }
            
        },
        generateAuth(){
            axios.get('https://vl0i36.deta.dev/admin/generate?quantity=1&is_super=1')
                .then(res=>{
                    this.login = Object.keys(res.data)[0];
                    this.password = res.data[Object.keys(res.data)[0]];
                })
        }
    },
    mounted(){
        this.isSuper();
    }
}
</script>

<style scoped>

</style>
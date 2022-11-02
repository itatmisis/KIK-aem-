<template>
    <div class="position-absolute top-50 start-50 translate-middle">
        <div class="p-5 rounded" style="background:white;width:25rem">
            <p class="h5">Вход в личный кабинет</p>
            <form>
                <div class="mb-3">
                    <label for="exampleInputEmail1" class="form-label">Логин</label>
                    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                    <label for="exampleInputPassword1" class="form-label">Пароль</label>
                    <input type="password" class="form-control" id="exampleInputPassword1">
                </div>
                <div class="row" style="margin-left:1%">
                    <button v-on:click="goToMain" class="col-sm btn" style="color:white;background:#444A60">Войти</button>
                    <div style="margin-left:5%" class="mt-2 col-sm-7 form-check">
                        <input type="checkbox" class="form-check-input" id="exampleCheck1">
                        <label class="form-check-label"  for="exampleCheck1">запомнить меня</label>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    methods:{
        goToMain(){
            this.$router.push('/')
        }
    }
}
</script>

<style scoped>
    
</style>
<template>
    <nav class="navbar" style="background:white">
        <div class="container-fluid">
            <span class="navbar-brand mt-2 row">
                <img class="col-sm-4" style="margin-left:5%" src="../assets/logo.svg" alt="">
                <form class="col-sm d-flex" style="margin-left:10%" role="search">
                    <input class="form-control me-2" type="search" placeholder="" aria-label="Search">
                    <button class="btn" style="color:white;background:#3E445B" type="submit">Поиск</button>
                </form> 
            </span>
            
            <a class="navbar-brand" style="cursor:pointer" href="#" v-on:click="goToProfile">
                <img src="../assets/avatar.svg" alt="Logo" height="44">
            </a>
        </div>
    </nav>
</template>

<script>
export default {
    methods:{
        goToProfile(){
            this.$router.push('/profile')
        }
    }
}
</script>

<style scoped>

</style>
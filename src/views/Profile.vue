<template>
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
    </div>
</template>

<script>
export default {
    data(){
        return{
            name: 'Аркадий Паровозов',
            jobTitle: 'Начальник какой-то'
        }
    }   
}
</script>

<style scoped>

</style>
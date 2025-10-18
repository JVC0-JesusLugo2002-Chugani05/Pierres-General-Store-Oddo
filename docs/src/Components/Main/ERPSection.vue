<script setup>
import Title from './Title.vue';
</script>

<template>
    <section>
        <Title url="/img/erp-elegido.png"/>
        <div class="row">
            <div class="col card p-0" id="card-1">
                <h2 class="p-2 display-6">¿Cuál?</h2>
                <p class="p-2">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Omnis eos illum voluptas quidem eius officia, quo fugit, fuga quas earum obcaecati illo libero fugiat natus labore ab! Veniam, fugit quod.</p>
            </div>
            <div class="col card p-0 mx-2" id="card-2"> 
                <h2 class="p-2 display-6">¿Por qué?</h2>
                <p class="p-2">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Omnis eos illum voluptas quidem eius officia, quo fugit, fuga quas earum obcaecati illo libero fugiat natus labore ab! Veniam, fugit quod.</p>
            </div>
            <div class="col card p-0" id="card-3">
                <h2 class="p-2 display-6">¿Cómo?</h2>
                <p class="p-2">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Omnis eos illum voluptas quidem eius officia, quo fugit, fuga quas earum obcaecati illo libero fugiat natus labore ab! Veniam, fugit quod.</p>
            </div>
        </div>
    </section>
</template>

<style scoped>
#card-1 {
    background-color: #F56C83;
}

#card-2 {
    background-color: #6C84F5;
}

#card-3 {
    background-color: #6CF585;
}

p {
    background-color: white;
    width: 100%;
    margin: 0;
}
</style>
<script setup>
import { defineProps } from 'vue';

const { url } = defineProps({ 
    url: String 
})
</script>

<template>
    <div class="title-container">
        <img :src="url" class="title">
    </div>
</template>

<style scope>
.title-container {
    width: 100%;
    height: 150px;
    overflow: hidden;
}
.title-container img {
    object-fit: cover;
    width: 100%;
    height: 100%;
}
</style>
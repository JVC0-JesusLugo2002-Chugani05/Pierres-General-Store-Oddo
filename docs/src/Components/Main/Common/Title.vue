<script setup>
import { defineProps } from 'vue'

const { filename } = defineProps({
  filename: String,
})
</script>

<template>
  <div class="title-container container pt-5">
    <img :src="'/img/titles/' + filename" class="title" />
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

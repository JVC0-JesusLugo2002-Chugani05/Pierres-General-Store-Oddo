<script setup>
const { title, imgUrl, description } = defineProps({
  title: String,
  imgUrl: String,
  description: String,
})
</script>

<template>
  <div class="col-3 mx-3 card">
    <img :src="imgUrl" class="card-img-top img-fluid" />
    <div class="card-body">
      <h3 class="card-title">{{ title }}</h3>
      <p class="card-text ">
        {{ description }}
      </p>
    </div>
  </div>
</template>

<script setup>
const { title, imgUrl, description } = defineProps({
  title: String,
  imgUrl: String,
  description: String,
})
</script>

<template>
  <div class="col-3 mx-4 card p-0 shadow">
    <img :src="imgUrl" class="card-img-top img-fluid" />
    <div class="card-body">
      <h3 class="card-title">{{ title }}</h3>
      <p class="card-text p-2">
        {{ description }}
      </p>
    </div>
  </div>
</template>

<style scoped>
.card {
  transition: 0.3s;
}
.card:hover {
  transform: scale(1.02);
}
</style>

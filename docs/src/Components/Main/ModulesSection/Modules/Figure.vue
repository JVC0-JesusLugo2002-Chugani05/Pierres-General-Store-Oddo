<script setup>
const { imgUrl, description } = defineProps({
    imgUrl: String,
    description: String
})
</script>

<template>
    <div class="row my-5 d-flex flex-column align-items-center">
      <img
        :src="imgUrl"
        :alt="description"
        class="img-fluid figure-img col-10"
      />
      <p class="figure-caption text-center">{{ description }}</p>
    </div>
</template>
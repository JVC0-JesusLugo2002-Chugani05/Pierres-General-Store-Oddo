<script setup>
const { titleUrl, image, githubUrl } = defineProps({
  titleUrl: String,
  image: String,
  githubUrl: String,
})
</script>

<template>
  <a
    :href="githubUrl"
    class="col-3 d-flex m-5 flex-column text-center justify-content-center text-decoration-none text-reset"
    target="_blank"
  >
    <img :src="image" alt="profile image" class="rounded-circle" />
    <img :src="titleUrl" alt="profile title" class="mt-3" />
  </a>
</template>

<style scoped>
a {
  transition: 0.3s;
}
a:hover {
  transform: scale(1.05);
}
</style>

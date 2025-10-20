<script setup>
const { title } = defineProps({
  id: String,
  title: String,
})
</script>

<template>
  <div class="col card p-0 mx-5 shadow-lg border-0 rounded" :id="id">
    <h2 class="p-3 display-6 m-0">
      <strong>{{ title }}</strong>
    </h2>
    <slot></slot>
  </div>
</template>

<style scoped>
#card-1 h2 {
  background-color: #f56c83;
}

#card-2 h2 {
  background-color: #6c84f5;
}

#card-3 h2 {
  background-color: #6cf585;
}
</style>

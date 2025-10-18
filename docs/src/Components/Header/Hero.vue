<script setup>
import ContentsList from './ContentsList.vue'
</script>

<template>
  <div class="hero container-fluid text-white d-flex flex-column">
    <div class="container">
      <div class="row">
        <div class="col">
          <h1 class="display-1">Pierre's General Store Odoo</h1>
        </div>
        <div class="col">
          <ContentsList />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.hero {
  height: 100vh;
  background-image: url('/img/hero.jpg');
  background-position-y: bottom;
  background-position-x: center;
}
.container {
  margin-top: 10vh;
}
.title {
  font-family: "Stardew Valley Title";
  font-size: 80px;
}
</style>

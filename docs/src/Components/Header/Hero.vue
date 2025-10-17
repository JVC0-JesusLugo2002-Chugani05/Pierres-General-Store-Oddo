<script setup>
import ContentsList from './ContentsList.vue'
</script>

<template>
  <div class="hero container-fluid text-white d-flex flex-column justify-content-center">
    <div class="container">
      <div class="row">
        <div class="col">
          <h1 class="display-1">Pierre's General Shop Odoo</h1>
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
  height: 50vh;
  background-image: url('/img/hero.png');
  background-position-y: center;
}
</style>

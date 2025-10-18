<script setup lang="ts">
import Hero from './Components/Header/Hero.vue'
import Title from './Components/Main/Title.vue'

import AboutSection from './Components/Main/AboutSection.vue'
import ERPSection from './Components/Main/ERPSection.vue'
</script>

<template>
  <header>
    <Hero />
  </header>
  <main class="container-fluid">
    <AboutSection />
    <ERPSection />
    <Title url="/img/modulos-utilizados.png" />
    <Title url="/img/problemas-resueltos.png" />
    <Title url="/img/autores.png" />
  </main>
  <footer></footer>
</template>

<style>
body {
  border: 0;
  padding: 0;
}
main {
  background-image: linear-gradient(#f4d26c, #a8914a);
}
@font-face {
  font-family: 'Stardew Valley Title';
  src:
    local('Stardew Valley Title'),
    url('./assets/fonts/Stardew-Valley-Regular.ttf') format('truetype');
}
@font-face {
  font-family: 'Stardew Valley';
  src:
    local('Stardew Valley'),
    url('./assets/fonts/StardewValley.ttf') format('truetype');
}
</style>

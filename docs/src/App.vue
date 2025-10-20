<script setup lang="ts">
import Hero from './Components/Header/Hero.vue'
import Title from './Components/Main/Common/Title.vue'

import AboutSection from './Components/Main/AboutSection/AboutSection.vue'
import ERPSection from './Components/Main/ERPSection/ERPSection.vue'
import ModulesSection from './Components/Main/ModulesSection/ModulesSection.vue'
</script>

<template>
  <header>
    <Hero />
  </header>
  <main class="container-fluid">
    <AboutSection />
    <ERPSection />
    <ModulesSection />
    <Title url="/img/problemas-resueltos.png" />
    <Title url="/img/autores.png" />
  </main>
  <footer></footer>
</template>

<style scoped>
body {
  border: 0;
  padding: 0;
}
header {
  background-color: #f4d26c;
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

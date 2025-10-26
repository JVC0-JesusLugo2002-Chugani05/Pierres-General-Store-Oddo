<script setup>
import Title from '../Common/Title.vue'
import AuthorItem from './AuthorItem.vue'

const profiles = [
  {
    titleUrl: 'img/authors/rashi-chugani.png',
    image: 'img/authors/rashi-chugani-avatar.png',
    githubUrl: 'https://github.com/Chugani05',
  },
  {
    titleUrl: 'img/authors/jesus-lugo.png',
    image: 'img/authors/jesus-lugo-avatar.png',
    githubUrl: 'https://github.com/JesusLugo2002',
  },
  {
    titleUrl: 'img/authors/joseph-castillo.png',
    image: 'img/authors/joseph-castillo-avatar.png',
    githubUrl: 'https://github.com/JVC0',
  },
]
</script>

<template>
  <section id="AuthorsSection">
    <Title filename="autores.png" />
    <div class="container">
      <div class="row d-flex justify-content-center">
        <AuthorItem
          v-for="profile in profiles"
          :titleUrl="profile.titleUrl"
          :image="profile.image"
          :githubUrl="profile.githubUrl"
        />
      </div>
    </div>
  </section>
</template>

<script setup>
import Title from '../Common/Title.vue'
import AuthorItem from './AuthorItem.vue'

const profiles = [
  {
    titleUrl: '/img/authors/rashi-chugani.png',
    image:
      'https://th.bing.com/th/id/R.3e77a1db6bb25f0feb27c95e05a7bc57?rik=07AQ3YRhkD3z8A&pid=ImgRaw&r=0',
    githubUrl: 'https://github.com/Chugani05',
  },
  {
    titleUrl: '/img/authors/jesus-lugo.png',
    image:
      'https://th.bing.com/th/id/R.3e77a1db6bb25f0feb27c95e05a7bc57?rik=07AQ3YRhkD3z8A&pid=ImgRaw&r=0',
    githubUrl: 'https://github.com/JesusLugo2002',
  },
  {
    titleUrl: '/img/authors/joseph-castillo.png',
    image:
      'https://th.bing.com/th/id/R.3e77a1db6bb25f0feb27c95e05a7bc57?rik=07AQ3YRhkD3z8A&pid=ImgRaw&r=0',
    githubUrl: 'https://github.com/JVC0',
  },
]
</script>

<template>
  <section id="AuthorsSection">
    <Title url="/img/autores.png" />
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

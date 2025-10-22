<script setup>
import Title from '../Common/Title.vue'
import ProblemItem from './ProblemItem.vue'

const problems = [
  {
    title: 'Administración de los clientes',
    imgUrl: 'https://developers.elementor.com/docs/assets/img/elementor-placeholder-image.png',
    description:
      'En la tienda de Pierre, uno de los pilares más importantes de su negocio es la cercanía que tiene con sus clientes, para mantener ello, se asegura de registrar sus cumpleaños en el calendario y de ofrecer descuentos en ellos para afianzar sus relaciones.',
  },
  {
    title: 'Control del flujo de compras y ventas',
    imgUrl: 'https://developers.elementor.com/docs/assets/img/elementor-placeholder-image.png',
    description:
      'La tienda trabaja con productos que entran y salen del inventario al día',
  },
  {
    title: 'Gestión del inventario',
    imgUrl: 'https://developers.elementor.com/docs/assets/img/elementor-placeholder-image.png',
    description:
      'Lorem ipsum dolor sit amet consectetur adipisicing elit. Aut voluptas perspiciatis nisi quia non quos, dicta, neque dolores, rem libero vero consequuntur incidunt. Incidunt odit qui, explicabo eius atque illo.',
  },
]
</script>

<template>
  <section id="ProblemsSection">
    <Title url="/img/problemas-resueltos.png" />
    <div class="container-fluid mt-3">
      <div class="row row-cols-3 d-flex justify-content-center">
        <ProblemItem
          v-for="problem in problems"
          :title="problem.title"
          :description="problem.description"
          :imgUrl="problem.imgUrl"
        />
      </div>
    </div>
  </section>
</template>

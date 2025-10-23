<script setup>
import Title from '../Common/Title.vue'
import ProblemItem from './ProblemItem.vue'

const problems = [
  {
    title: 'Administración de los clientes',
    imgUrl: '/img/problems-banners/calendar.png',
    description:
      'En la tienda de Pierre, uno de los pilares más importantes de su negocio es la cercanía que tiene con sus clientes, para mantener ello, se asegura de registrar sus cumpleaños en el módulo de calendario y de ofrecer descuentos en ellos para afianzar sus relaciones.',
  },
  {
    title: 'Gestión del inventario',
    imgUrl: 'img/problems-banners/inventory.png',
    description:
      'El diario y rápido movimiento del inventario implica con ello una buena administración del mismo, por lo tanto, gracias al módulo de inventario y sus útiles funcionalidades, Pierres ha podido gestionar de una forma más limpia y eficaz el inventario de su negocio.',
  },
  {
    title: 'Control del flujo de compras y ventas',
    imgUrl: '/img/problems-banners/selling-items.png',
    description:
      'La tienda trabaja con productos que entran y salen del inventario al día y estos movimientos requieren de un control y un registro necesario para salvaguardar los datos que más adelante pueden ser usados, por lo tanto, Pierre hace uso de los módulos de ventas y compras para gestionar y facilitarse el trabajo.',
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

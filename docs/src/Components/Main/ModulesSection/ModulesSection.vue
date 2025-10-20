<script setup>
import Title from '../Common/Title.vue'
import ModuleCard from './ModuleCard.vue'

const modules = [
  {
    id: 'facturacion',
    title: 'Facturación y contabilidad',
    imgUrl: '/img/modules-icons/facturacion.svg',
    description:
      'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos laborum officia iusto ipsa doloremque. Cumque odio, nostrum ea dolor sit facilis id dolore culpa deleniti perspiciatis adipisci. Nobis, neque laborum!',
  },
  {
    id: 'empleados',
    title: 'Empleados',
    imgUrl: '/img/modules-icons/empleados.svg',
    description:
      'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos laborum officia iusto ipsa doloremque. Cumque odio, nostrum ea dolor sit facilis id dolore culpa deleniti perspiciatis adipisci. Nobis, neque laborum!',
  },
  {
    id: 'compras',
    title: 'Compras',
    imgUrl: '/img/modules-icons/compras.svg',
    description:
      'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos laborum officia iusto ipsa doloremque. Cumque odio, nostrum ea dolor sit facilis id dolore culpa deleniti perspiciatis adipisci. Nobis, neque laborum!',
  },
  {
    id: 'ventas',
    title: 'Ventas',
    imgUrl: '/img/modules-icons/ventas.svg',
    description:
      'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos laborum officia iusto ipsa doloremque. Cumque odio, nostrum ea dolor sit facilis id dolore culpa deleniti perspiciatis adipisci. Nobis, neque laborum!',
  },
  {
    id: 'punto-de-venta',
    title: 'Punto de venta',
    imgUrl: '/img/modules-icons/punto-de-venta.svg',
    description:
      'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos laborum officia iusto ipsa doloremque. Cumque odio, nostrum ea dolor sit facilis id dolore culpa deleniti perspiciatis adipisci. Nobis, neque laborum!',
  },
  {
    id: 'inventario',
    title: 'Inventario',
    imgUrl: '/img/modules-icons/inventory.svg',
    description:
      'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos laborum officia iusto ipsa doloremque. Cumque odio, nostrum ea dolor sit facilis id dolore culpa deleniti perspiciatis adipisci. Nobis, neque laborum!',
  },
  {
    id: 'crm',
    title: 'CRM',
    imgUrl: '/img/modules-icons/crm.svg',
    description:
      'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos laborum officia iusto ipsa doloremque. Cumque odio, nostrum ea dolor sit facilis id dolore culpa deleniti perspiciatis adipisci. Nobis, neque laborum!',
  },
  {
    id: 'calendario',
    title: 'Calendario',
    imgUrl: '/img/modules-icons/calendario.svg',
    description:
      'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos laborum officia iusto ipsa doloremque. Cumque odio, nostrum ea dolor sit facilis id dolore culpa deleniti perspiciatis adipisci. Nobis, neque laborum!',
  },
]
</script>

<template>
  <section id="ModulesSection">
    <Title url="/img/modulos-utilizados.png" />
    <div class="container-fluid">
      <div class="row row-cols-3 g-5 d-flex justify-content-center">
        <ModuleCard
          v-for="module in modules"
          :id="module.id"
          :title="module.title"
          :imgUrl="module.imgUrl"
          :description="module.description"
        />
      </div>
    </div>
  </section>
</template>

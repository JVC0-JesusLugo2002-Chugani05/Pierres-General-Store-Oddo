<script setup>
import Title from '../Common/Title.vue'
import ModuleCard from './ModuleCard.vue'

const modules = [
  {
    id: 'facturacion',
    title: 'Facturación y contabilidad',
    iconUrl: '/img/modules-icons/facturacion.svg',
  },
  {
    id: 'empleados',
    title: 'Empleados',
    iconUrl: '/img/modules-icons/empleados.svg',
  },
  {
    id: 'compras',
    title: 'Compras',
    iconUrl: '/img/modules-icons/compras.svg',
  },
  {
    id: 'ventas',
    title: 'Ventas',
    iconUrl: '/img/modules-icons/ventas.svg',
  },
  {
    id: 'punto-de-venta',
    title: 'Punto de venta',
    iconUrl: '/img/modules-icons/punto-de-venta.svg',
  },
  {
    id: 'inventario',
    title: 'Inventario',
    iconUrl: '/img/modules-icons/inventory.svg',
  },
  {
    id: 'crm',
    title: 'CRM',
    iconUrl: '/img/modules-icons/crm.svg',
  },
  {
    id: 'calendario',
    title: 'Calendario',
    iconUrl: '/img/modules-icons/calendario.svg',
  },
  {
    id: 'tema-app',
    title: 'Tema backend',
    iconUrl: '/img/modules-icons/jumino.png',
  },
]
</script>

<template>
  <section id="ModulesSection">
    <Title url="/img/modulos-utilizados.png" />
    <div class="container my-5">
      <div class="row row-cols-3 g-5 d-flex justify-content-center">
        <ModuleCard
          v-for="module in modules"
          :id="module.id"
          :title="module.title"
          :iconUrl="module.iconUrl"
        />
      </div>
    </div>
  </section>
</template>

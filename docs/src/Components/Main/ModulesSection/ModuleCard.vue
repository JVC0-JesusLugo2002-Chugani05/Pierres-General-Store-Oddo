<script setup>
import Calendario from './Modules/Calendario.vue'
import Compras from './Modules/Compras.vue'
import CRM from './Modules/CRM.vue'
import Empleados from './Modules/Empleados.vue'
import Facturacion from './Modules/Facturacion.vue'
import Inventario from './Modules/Inventario.vue'
import PuntoDeVenta from './Modules/PuntoDeVenta.vue'
import Tema from './Modules/Tema.vue'
import Ventas from './Modules/Ventas.vue'

const { id, title, iconUrl } = defineProps({
  id: String,
  title: String,
  iconUrl: String,
})
</script>

<template>
  <button
    type="button"
    :id="id"
    class="card mx-3 col-2 shadow border-dark rounded-5"
    data-bs-toggle="modal"
    :data-bs-target="'#' + id + 'Modal'"
  >
    <div class="card-body d-flex flex-column justify-content-center align-items-center">
      <img class="img-fluid" :src="iconUrl" :alt="id + ' icon'" />
      <p class="lead fw-bold">
        {{ title }}
      </p>
    </div>
  </button>

  <div class="modal fade" :id="id + 'Modal'" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-3" id="exampleModalLabel">
            <img :src="iconUrl" :alt="id + ' icon in modal'" class="mx-2" />
            {{ title }}
          </h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <Facturacion v-if="id == 'facturacion'" />
        <Empleados v-else-if="id == 'empleados'" />
        <Compras v-else-if="id == 'compras'" />
        <Ventas v-else-if="id == 'ventas'" />
        <PuntoDeVenta v-else-if="id == 'punto-de-venta'" />
        <Inventario v-else-if="id == 'inventario'" />
        <CRM v-else-if="id == 'crm'" />
        <Calendario v-else-if="id == 'calendario'" />
        <Tema v-else />
      </div>
    </div>
  </div>
</template>

<style scoped>
.card {
  transition: 0.3s;
}

.card:hover {
  transform: scale(1.05);
}

img {
  width: 64px;
}
</style>

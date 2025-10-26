<script setup>
import Figure from './Figure.vue'
</script>

<template>
  <div class="card-body text-dark fs-5 p-5">
    <Figure imgUrl="calendario/vista-general.png" description="Vista general del calendario" />
    <p>
      Por último, el módulo de calendario le permite a Pierre gestionar mejor su tiempo y preparar
      recursos para la celebración de eventos en el pueblo, registrar los cumpleaños de sus clientes
      para ofrecer regalos y descuentos, y programar las reuniones desde un único punto de la
      aplicación.
    </p>
    <Figure imgUrl="calendario/edicion-de-eventos.png" description="Edición de un evento" />
    <Figure
      imgUrl="calendario/sincronizacion-con-otros-servicios.png"
      description="Sincronización con Outlook y Google Calendar"
    />
  </div>
</template>

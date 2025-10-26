<script setup>
import Figure from './Figure.vue'
</script>

<template>
  <div class="card-body fs-5 text-dark p-5">
    <Figure imgUrl="crm/vista-general.png" description="Vista general del módulo" />
    <p>
      La aplicación de CRM es de las herramientas más útiles para el negocio de Pierre, pues es la
      que le permite enfocarse en sus clientes y necesidades de ventas, llevando el seguimiento de
      oportunidades con una organización eficiente gracias a la vista de Kanban. Pierre, desde esta
      plataforma, puede programar llamadas, envios de presupuestos y reuniones con facilidad
      manteniendo una comunicación fluida y eficaz.
    </p>
    <Figure
      imgUrl="crm/pronostico.png"
      description="Pronóstico y resumen de las oportunidades por fechas "
    />
    <Figure
      imgUrl="crm/recurrentes.png"
      description="Capacidad de crear oportunidades recurrentes"
    />
  </div>
</template>

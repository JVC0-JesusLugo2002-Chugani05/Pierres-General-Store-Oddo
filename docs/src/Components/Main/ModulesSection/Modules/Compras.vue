<script setup>
import Figure from './Figure.vue'
</script>

<template>
  <div class="card-body fs-5 text-dark p-5">
    <Figure
      imgUrl="/img/modules-modals/compras/resumen.png"
      description="Gestor de solicitudes de presupuesto"
    />
    <p>
      Gestiona desde solicitudes de presupuesto hasta recepciones en un solo lugar. Gracias a este
      módulo, Pierre simplifica y automatiza los pedidos de compra con reglas de reabastecimiento,
      acuerdos personalizables y crea facturas de proveedor con mucha facilidad.
    </p>
    <Figure
      imgUrl="/img/modules-modals/compras/proveedores.png"
      description="Listado de proveedores"
    />
    <Figure
      imgUrl="/img/modules-modals/compras/solicitud-presupuesto.png"
      description="Detalles de una solicitud de presupuesto"
    />
  </div>
</template>

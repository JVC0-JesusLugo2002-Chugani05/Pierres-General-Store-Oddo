<script setup>
import Figure from './Figure.vue'
</script>

<template>
  <div class="card-body fs-5 text-dark p-5">
    <Figure imgUrl="ventas/vista-general.png" description="Vista general de ventas" />
    <p>
      Un creador de presupuestos claros, profesionales e interactivos. Gracias a este módulo, Pierre
      aplica de forma automática los precios e impuestos adecuados para cada cliente y puede
      visualizar todo bajo métricas personalizables, adaptables a sus necesidades.
    </p>
    <Figure imgUrl="ventas/analisis-clientes.png" description="Estadísiticas de clientes" />
    <Figure
      imgUrl="ventas/analisis-productos.png"
      description="Estadísticas de productos vendidos"
    />
  </div>
</template>

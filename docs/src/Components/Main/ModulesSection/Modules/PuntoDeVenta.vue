<script setup>
import Figure from './Figure.vue';
</script>

<template>
  <div class="card-body fs-5 text-dark p-5">
    <Figure imgUrl="punto-de-venta/vista-general.png" description="Vista general de una sesión"/>
    <p>
      El módulo de punto de venta ofrece un aplicativo intuitivo, confiable, con la capacidad de
      operar sin conexión, con una amplia gama de opciones para satisfacer las necesidades diarias
      de su tienda. La interfaz intuitiva facilita el aprendizaje para su uso y puede ser
      configurada fácilmente, e incluso Pierre disfruta de las opciones que tiene para mejorar la
      experiencia de compra mediante programas de fidelización y recompensas.
    </p>
    <Figure imgUrl="punto-de-venta/pago.png" description="Pantalla de pagos intuitivas"/>
    <Figure imgUrl="punto-de-venta/factura.png" description="Facturas personalizadas"/>
    <Figure imgUrl="punto-de-venta/cierre-de-sesion.png" description="Cierre de sesión con estadísticas básicos"/>
    <Figure imgUrl="punto-de-venta/informes.png" description="Informe de ventas diario"/>
  </div>
</template>

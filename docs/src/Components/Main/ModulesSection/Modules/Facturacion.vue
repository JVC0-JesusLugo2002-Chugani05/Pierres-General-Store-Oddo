<script setup>
import Figure from './Figure.vue'
</script>

<template>
  <div class="card-body fs-5 text-dark p-5">
    <Figure
      imgUrl="facturacion/vista-general.png"
      description="Vista general de facturas de clientes"
    />
    <p>
      Este módulo facilita la creación y personalización de facturas gracias a la disposición de
      elementos esenciales como la información del cliente, productos, precios y demás. Con este
      módulo, Pierre puede emitir facturas, actualizar estados de pagos o incluso crear pagos en
      lote para las facturas de sus proveedores, los granjeros de Pelican Town.
    </p>
    <Figure
      imgUrl="facturacion/control-factura-proveedor.png"
      description="Detalles de una factura de proveedor"
    />
    <Figure
      imgUrl="facturacion/analisis-facturas.png"
      description="Informe de análisis de facturas"
    />
  </div>
</template>

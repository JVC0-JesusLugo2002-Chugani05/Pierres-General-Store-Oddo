<script setup>
import Title from '../Common/Title.vue'
import ModuleCard from './ModuleCard.vue'

const modules = [
  {
    id: 'facturacion',
    title: 'Facturación y contabilidad',
    iconUrl: '/img/modules-icons/facturacion.svg',
    description:
      'Este módulo facilita la creación y personalización de facturas gracias a la disposición de elementos esenciales como la información del cliente, productos, precios y demás. Con este módulo, Pierre puede emitir facturas, actualizar estados de pagos o incluso crear pagos en lote para las facturas de sus proveedores, los granjeros de Pelican Town.',
  },
  {
    id: 'empleados',
    title: 'Empleados',
    iconUrl: '/img/modules-icons/empleados.svg',
    description:
      'La valiosa centralización de los procesos de recursos humanos es lo que ofrece este módulo. Pierre tendrá gracias a esto una vista general de los departamentos de su negocio, una clara clasificación de sus empleados por su información, una protección de datos privados gracias a los ajustes de acceso restringido y un control de las solicitudes de permisos y los plazos de ausencia.',
  },
  {
    id: 'compras',
    title: 'Compras',
    iconUrl: '/img/modules-icons/compras.svg',
    description:
      'Gestiona desde solicitudes de presupuesto hasta recepciones en un solo lugar. Gracias a este módulo, Pierre simplifica y automatiza los pedidos de compra con reglas de reabastecimiento, acuerdos personalizables y crea facturas de proveedor con mucha facilidad.',
  },
  {
    id: 'ventas',
    title: 'Ventas',
    iconUrl: '/img/modules-icons/ventas.svg',
    description:
      'Un creador de presupuestos claros, profesionales e interactivos. Pierre gestiona sus pedidos de venta, servicios y comercio en linea en una sola plataforma. Gracias a este módulo, se aplica de forma automática los precios e impuestos adecuados para cada cliente, y permitiendo el acceso al cliente, estos pueden visualizar sus documentos, ahorrando tiempo con el uso de firmas electrónicas para cerrar acuerdos.',
  },
  {
    id: 'punto-de-venta',
    title: 'Punto de venta',
    iconUrl: '/img/modules-icons/punto-de-venta.svg',
    description:
      'El módulo de punto de venta ofrece un aplicativo intuitivo, confiable, con la capacidad de operar sin conexión, con una amplia gama de opciones para satisfacer las necesidades diarias de su tienda. La interfaz intuitiva facilita el aprendizaje para su uso y puede ser configurada fácilmente, e incluso Pierre disfruta de las opciones que tiene para mejorar la experiencia de compra mediante programas de fidelización, recompensas y tarjetas de descuento.',
  },
  {
    id: 'inventario',
    title: 'Inventario',
    iconUrl: '/img/modules-icons/inventory.svg',
    description:
      'Pierre, gracias al módulo de inventario, puede ver en tiempo real el stock de su tienda y agiliza sus operaciones de forma eficaz, utilizando estrategias de rotación alta para un mercado de cambio rápido como el de la agricultura local, gestionando a su vez los envios entrantes y salientes.',
  },
  {
    id: 'crm',
    title: 'CRM',
    iconUrl: '/img/modules-icons/crm.svg',
    description:
      'La aplicación de CRM es de las herramientas más útiles para el negocio de Pierre, pues es la que le permite enfocarse en sus clientes y necesidades de ventas, llevando el seguimiento de oportunidades con una organización eficiente gracias a la vista de Kanban. Pierre, desde esta plataforma, puede programar llamadas, envios de presupuestos y reuniones con facilidad manteniendo una comunicación fluida y eficaz.',
  },
  {
    id: 'calendario',
    title: 'Calendario',
    iconUrl: '/img/modules-icons/calendario.svg',
    description:
      'Por último, el módulo de calendario le permite a Pierre gestionar mejor su tiempo y preparar recursos para la celebración de eventos en el pueblo, registrar los cumpleaños de sus clientes para ofrecer regalos y descuentos, y programar las reuniones desde un único punto de la aplicación.',
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
          :iconUrl="module.iconUrl"
          :description="module.description"
        />
      </div>
    </div>
  </section>
</template>

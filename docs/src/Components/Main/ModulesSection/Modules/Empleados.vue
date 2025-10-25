<script setup>
import Figure from './Figure.vue'
</script>

<template>
  <div class="card-body fs-5 text-dark p-5">
    <Figure
      imgUrl="empleados/vista-general.png"
      description="Vista general de empleados"
    />
    <p>
      La valiosa centralización de los procesos de recursos humanos es lo que ofrece este módulo.
      Pierre tendrá gracias a esto una vista general de los departamentos de su negocio, una clara
      clasificación de sus empleados por su información, una protección de datos privados gracias a
      los ajustes de acceso restringido y un control de las solicitudes de permisos y los plazos de
      ausencia.
    </p>
    <Figure
      imgUrl="empleados/departamentos.png"
      description="Organigrama de departamentos"
    />
    <Figure
      imgUrl="empleados/detalles-empleado.png"
      description="Detalles de un empleado"
    />
  </div>
</template>

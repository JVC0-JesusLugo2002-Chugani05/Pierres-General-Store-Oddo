<script setup>
import Figure from './Figure.vue'
</script>

<template>
  <div class="card-body fs-5 text-dark p-5">
    <Figure imgUrl="empleados/vista-general.png" description="Vista general de empleados" />
    <p>
      La valiosa centralización de los procesos de recursos humanos es lo que ofrece este módulo.
      Pierre tendrá gracias a esto una vista general de los departamentos de su negocio, una clara
      clasificación de sus empleados por su información, una protección de datos privados gracias a
      los ajustes de acceso restringido y un control de las solicitudes de permisos y los plazos de
      ausencia.
    </p>
    <Figure imgUrl="empleados/departamentos.png" description="Organigrama de departamentos" />
    <Figure imgUrl="empleados/detalles-empleado.png" description="Detalles de un empleado" />
    <p>
      El módulo de empleados puede ser enriquecido con otros módulos extras,
      <b>Asistencias / Ausencias</b>. Estos permiten el control de las asistencias de forma manual o
      automática (haciendo uso de credenciales) y la gestión y asignaciónd de ausencias de distintos
      tipos como por vacaciones o enfermedades.
    </p>
    <Figure
      imgUrl="empleados/escaner-asistencia.png"
      description="Escaner de código de barras de credenciales para asistencia"
    />
    <Figure
      imgUrl="empleados/employee-credential.png"
      description="Credenciales generadas por Odoo para un empleado"
    />
    <Figure
      imgUrl="empleados/resumen-ausencias.png"
      description="Resumen del módulo de ausencias"
    />
    <Figure
      imgUrl="empleados/asignacion-vacaciones.png"
      description="Formulario de asignación de ausencia"
    />
  </div>
</template>

<template>
  <button
    class="col use border-0 d-flex justify-content-center align-items-center display-5"
    data-bs-toggle="modal"
    data-bs-target="#useBackupModal"
  >
    <p class="bg-light rounded w-50">Cómo usar</p>
  </button>

  <div class="modal fade" id="useBackupModal" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered modal-lg modal-dialog-scrollable">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-3" id="useBackupModalLabel">
            Cómo usar una copia de seguridad
          </h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="row d-flex justify-content-center">
            <p>
              Para reestablecer una base de datos haciendo uso de una copia de seguridad, debemos
              tener disponible dicha copia como un archivo comprimido que es lo que se le enviará al
              gestor para reestablecer los datos. Esta puede tener la <i>filestore</i> o no
              (directorio donde se almacenan las imágenes).
            </p>
            <p>
              Cuando accedemos a Odoo, nos dirigimos a la pantalla de restaurar una base de datos
              (mediante la pantalla de inicio de sesión o el gestor de bases de datos)
            </p>
            <img
              src="/img/erp-section/how-backup.png"
              alt="Database management"
              class="img-fluid my-3"
            />
            <p>Y tras darle al botón nos abrirá un formulario para cargar la copia de seguridad:</p>
            <img
              src="/img/erp-section/restore-backup-form.png"
              alt="Backup loading"
              class="img-fluid w-50 my-3"
            />
            <p>
              Debemos ingresar una contraseña maestra, el archivo a cargar y el nombre nuevo de la
              base de datos. También deberemos indicar si estamos copiando o moviendo la base de
              datos. Después de esto podremos acceder a nuestra base de datos
            </p>
            <div class="alert alert-primary w-100 text-center" role="alert">
              <i class="bi bi-info-circle"></i> La opción <i>neutralize</i> es para cargar una base
              de datos neutralizada que,
              <a
                href="https://www.odoo.com/documentation/17.0/administration/neutralized_database.html"
                >según la misma documentación de Odoo</a
              >:
              <i
                >Una base de datos neutralizada es una base de datos no productiva en la que se
                desactivan varios parámetros. Esto permite realizar pruebas sin riesgo.</i
              >
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.use {
  width: 20vw;
  height: 20vw;
  background-position: center;
  filter: grayscale(50%);
  transition: 0.3s;
  background-image: url('/img/backup-section/use-background.webp');
}
.use:hover {
  filter: grayscale(0%);
}
</style>

<template>
  <button
    class="col create border-0 d-flex justify-content-center align-items-center display-5"
    data-bs-toggle="modal"
    data-bs-target="#createBackupModal"
  >
    <p class="bg-light rounded w-50">Cómo crear</p>
  </button>

  <div class="modal fade" id="createBackupModal" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-3" id="createBackupModalLabel">
            <i class="bi bi-floppy"></i> Cómo crear una copia de seguridad
          </h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <p>
              Para crear la copia de seguridad, debemos
              <b>acceder al menú de gestión de bases de datos de Odoo</b>. Para ello,
              <b>debemos cerrar nuestra sesión (si tenemos alguna activa)</b>. Esto nos redirigirá
              al siguiente menú:
            </p>
            <img
              src="/img/erp-section/how-backup.png"
              alt="Database management menu"
              class="img-fluid my-3"
            />
            <p>
              Y al darle la opción de
              <span class="text-primary fw-bold"><i class="bi bi-floppy"></i> Backup</span>, nos
              aparecerá el siguiente formulario:
            </p>
            <img src="/img/erp-section/backup-form.png" alt="Backup form" class="img-fluid my-3" />
            <p>
              Una vez ingresada la contraseña maestra y el tipo de archivo a exportar, directamente
              descargará la copia de seguridad en nuestro dispositivo.
            </p>
            <div class="alert alert-primary w-100 text-center" role="alert">
              <i class="bi bi-card-image"></i> Importante saber que en <i>filestore</i> es donde se
              almacenan las imágenes de las bases de datos.
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.create {
  width: 20vw;
  height: 20vw;
  background-position: center;
  filter: grayscale(50%);
  transition: 0.3s;
  background-image: url('/img/backup-section/create-background.jpeg');
}
.create:hover {
  filter: grayscale(0%);
}
</style>

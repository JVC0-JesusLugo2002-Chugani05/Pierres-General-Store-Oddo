<script setup>
const installationScript = `cat << EOF > docker-compose.yml
services:
    web:
        image: odoo:17
        depends_on:
            - db
        ports:
        - 8069:8069
        volumes:
        - ./odoo/filestore/:/var/lib/odoo/filestore
        - ./odoo/sessions/:/var/lib/odoo/sessions
        - ./addons:/mnt/extra-addons
        environment:
        - HOST=db
        - USER=odoo
        - PASSWORD=odoo
        user: root
        command: --dev=all 
    db:
        image: postgres:15
        environment:
        - POSTGRES_PASSWORD=odoo
        - POSTGRES_USER=odoo
        - POSTGRES_DB=postgres
        volumes:
        - ./database:/var/lib/postgresql/data
EOF`
</script>

<template>
  <button
    id="instructions-button"
    type="button"
    class="btn btn-lg btn-light w-100 position-absolute bottom-0"
    data-bs-toggle="modal"
    data-bs-target="#installationModal"
  >
    <i class="bi bi-book"></i> Instrucciones
  </button>

  <div
    class="modal fade"
    id="installationModal"
    tabindex="-1"
    aria-labelledby="installationModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered modal-xl modal-dialog-scrollable">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="installationModalLabel">
            <i class="bi bi-book"></i> Instrucciones
          </h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <h4 class="my-2">Requerimientos</h4>
          El único requisito necesario es <b>Docker Compose</b> en el ordenador y permisos de
          administración para la gestión completa de los ficheros de la base de datos y
          configuración.
          <h4 class="my-2">Instalación</h4>
          <ol class="list-group list-group-numbered">
            <li class="list-group-item fw-bold">
              Creamos un directorio donde tendremos nuestros archivos y accedemos a él. Por ejemplo,
              podemos escribir en la terminal:<br />
              <code> mkdir ~/MyOdoo && cd ~/MyOdoo </code>
            </li>
            <li class="list-group-item fw-bold">
              Luego ejecuta esto en la misma terminal para crear el archivo
              <i>docker-compose.yml</i> con su contenido: <br />
              <pre>{{ installationScript }}</pre>
            </li>
            <li class="list-group-item fw-bold">
              Ahora podemos levantar el servicio con <code>docker compose up -d --build</code> y
              pararlo con <code>docker compose down</code>.
            </li>
            <li class="list-group-item fw-bold">
              Una vez levantado al servicio, podemos acceder a él en
              <a href="localhost:8069">Localhost:8069</a> (suponiendo que no has cambiado el puerto
              en el <i>docker-compose.yml</i>)
            </li>
            <li class="list-group-item fw-bold">
              Dentro del sitio web nos encontraremos con dos opciones: crear una nueva base de datos
              completando el formulario, o reestableciendo una desde una copia de seguridad. (Los
              detalles para el uso de una copia de seguridad se encuentran más adelante).
              <img
                src="/img/erp-section/signup-database.png"
                alt="Database signup form"
                class="w-50 mt-2"
              />
            </li>
            <li class="list-group-item fw-bold">
              Una vez creada (o reestablecida) la base de datos, nos redirigirá a un formulario de
              inicio de sesión como este para insertar nuestras credenciales y acceder finalmente.
              <br />
              <img
                src="/img/erp-section/login-database.png"
                alt="Database login form"
                class="w-50 mt-2"
              />
            </li>
          </ol>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
pre {
  color: #d63384;
}
#instructions-button {
  background-color: #6cf585;
}
#instructions-button:hover {
  background-color: #5ddd74;
}
</style>

<script setup>
import ERPCard from './ERPCard.vue'
import Title from './Title.vue'

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
  <section id="ERPSection">
    <Title url="/img/erp-elegido.png" />
    <div class="row">
      <ERPCard id="card-1" title="¿Cuál?">
        <div class="h-100">
          <p class="p-3 lead">
            Tras haber realizado observaciones en el caso de Pierre hemos decidido usar
            <strong>Odoo</strong> como ERP, una plataforma de software empresarial de
            <b>código abierto</b> que centraliza las diferentes areas del negocio.
          </p>
          <a
            id="odoo-button"
            href="https://www.odoo.com/es_ES"
            class="btn btn-light btn-lg w-100 position-absolute bottom-0"
            ><i class="bi bi-box-arrow-up-right"></i> Ir a Odoo.com</a
          >
        </div>
      </ERPCard>
      <ERPCard id="card-2" title="¿Por qué?">
        <p class="p-3 lead">
          El caso de Pierre demanda con urgencia de un ERP pues la naturaleza creciente del mercado
          local aumentará su flujo de entrada/salida rápidamente y
          <b>debe tener un presente un robusto sistema de gestión</b> que le facilite la
          organización de las areas a trabajar como empresario. Por la velocidad de cambio y de
          aparición de distintas necesidades,
          <b>Odoo brilla gracias a su sistema modular de aplicaciones y la escalabilidad</b> que
          esto conlleva.
        </p>
      </ERPCard>
      <ERPCard id="card-3" title="¿Cómo?">
        <div class="h-100">
          <p class="p-3 lead">
            La implementación de Odoo se llevará a cabo mediante el uso de Docker Compose, haciendo
            uso de una imagen de Odoo oficial junto al de PostgreSQL como base de datos.
          </p>
          <button
            id="instructions-button"
            type="button"
            class="btn btn-lg btn-light w-100 position-absolute bottom-0"
            data-bs-toggle="modal"
            data-bs-target="#installationModal"
          >
            <i class="bi bi-book"></i> Instrucciones
          </button>
        </div>
      </ERPCard>
    </div>
  </section>

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
          <ol>
            <li>
              <p class="fw-bold">
                Creamos un directorio donde tendremos nuestros archivos y accedemos a él. Por
                ejemplo:
              </p>
              <code> mkdir ~/MyOdoo && cd ~/MyOdoo </code>
            </li>
            <li>
              <p class="fw-bold">
                Luego ejecuta esto para crear el archivo <i>docker-compose.yml</i> con su contenido:
              </p>
              <pre>{{ installationScript }}</pre>
            </li>
            <li>
                <p class="fw-bold">Ahora podemos levantar el servicio con <code>docker compose up -d --build</code> y pararlo con <code>docker compose down</code>.</p>
            </li>
            <li><p class="fw-bold">Una vez levantado al servicio, podemos acceder a él en <a href="localhost:8069">Localhost:8069</a> (suponiendo que no has cambiado el puerto en el <i>docker-compose.yml</i>)</p></li>
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
p {
  background-color: white;
  width: 100%;
  margin: 0;
}

#instructions-button {
  background-color: #6cf585;
}
#instructions-button:hover {
  background-color: #5ddd74;
}

pre {
    color: #d63384;
}

#odoo-button {
  background-color: #f56c83;
}
#odoo-button:hover {
  background-color: #ef8596;
}
</style>

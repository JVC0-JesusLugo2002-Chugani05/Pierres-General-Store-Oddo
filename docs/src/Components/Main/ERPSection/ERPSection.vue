<script setup>
import ERPCard from './ERPCard.vue'
import Title from '../Common/Title.vue'
import Instructions from './Instructions.vue'
</script>

<template>
  <section id="ERPSection">
    <Title filename="erp-elegido.png" />
    <div class="row">
      <ERPCard id="card-1" title="¿Cuál?">
        <div class="h-100">
          <p class="p-3">
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
        <p class="p-3">
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
          <p class="p-3">
            La implementación de Odoo se llevará a cabo mediante el uso de Docker Compose, haciendo
            uso de una imagen de Odoo oficial junto al de PostgreSQL como base de datos.
          </p>
          <Instructions />
        </div>
      </ERPCard>
    </div>
  </section>
</template>

<style scoped>
p {
  background-color: white;
  width: 100%;
  margin: 0;
}

#odoo-button {
  background-color: #f56c83;
}
#odoo-button:hover {
  background-color: #ef8596;
}
</style>

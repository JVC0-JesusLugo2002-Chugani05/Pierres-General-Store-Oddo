<script setup>
import Title from './Title.vue'
</script>

<template>
  <section class="container" id="AboutSection">
    <Title url="/img/la-tienda-de-pierre.png" />
    <div class="card p-5 shadow-lg rounded-5">
      <div class="row">
        <div class="col text-justify">
          <p>
            En el pequeño y rural <b>Pueblo Pelícano, Stardew Valley</b>, su estabilidad económica
            está practicamente basada en el comercio local de productos agrícolas gracias a sus
            fértiles extensiones de tierra y las ágiles manos de los granjeros que habitan en este
            pequeño pueblo.
          </p>
          <p>
            Por esto mismo, <b>la tienda de Pierre</b> es uno de los focos importantes de la
            economía del pueblo, pues
            <b>es el proveedor principal de productos como semillas y fertilizante</b>, así como
            también <b>quién compra los productos frescos a los granjeros para exportarlos</b> más
            allá del pueblo.
          </p>
          <button
            type="button"
            data-bs-toggle="modal"
            class="border-0 btn btn-outline-success fw-bold"
            data-bs-target="#locationModal"
          >
            <i class="bi bi-pin-map"></i> Ubicación
          </button>
        </div>
        <div class="col-3 text-center">
          <figure class="figure">
            <img src="/img/pierre-portrait.jpeg" alt="Pierre portrait" class="figure-img rounded" />
            <figcaption class="figure-caption">Pierre, dueño de la tienda</figcaption>
          </figure>
        </div>
      </div>
    </div>
  </section>

  <div
    class="modal fade"
    id="locationModal"
    tabindex="-1"
    aria-labelledby="locationModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered modal-xl">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="locationModalLabel">
            <i class="bi bi-pin-map"></i> Ubicación
          </h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body d-flex justify-content-around align-items-center">
          <figure class="figure text-center">
            <img src="/img/pierre-shop.png" alt="" class="img-fluid" />
            <figcaption class="figure-caption">Tienda de Pierre</figcaption>
          </figure>
          <figure class="figure text-center">
            <img src="/img/pierre-location.png" alt="" class="img-fluid" />
            <figcaption class="figure-caption">Ubicación en Pueblo Pelícano</figcaption>
          </figure>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
section {
  font-size: 20px;
}
</style>

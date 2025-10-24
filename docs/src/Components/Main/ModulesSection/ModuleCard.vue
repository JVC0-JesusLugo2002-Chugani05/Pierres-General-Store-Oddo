<script setup>
const { id, title, iconUrl, description } = defineProps({
  id: String,
  title: String,
  iconUrl: String,
  description: String,
})
</script>

<template>
  <button
    type="button"
    :id="id"
    class="card mx-3 col-2 shadow border-dark rounded-5"
    data-bs-toggle="modal"
    :data-bs-target="'#' + id + 'Modal'"
  >
    <div class="card-body d-flex flex-column justify-content-center align-items-center">
        <img class="img-fluid" :src="iconUrl" :alt="id + ' icon'" />
        <p class="lead fw-bold">
          {{ title }}
        </p>
    </div>
  </button>

  <div class="modal fade" :id="id + 'Modal'" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-3" id="exampleModalLabel">
            <img :src="iconUrl" :alt="id + ' icon in modal'" class="mx-2" />
            {{ title }}
          </h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body lead">
          {{ description }}
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card {
  transition: 0.3s;
}

.card:hover {
  transform: scale(1.05);
}

img {
  width: 64px;
}
</style>

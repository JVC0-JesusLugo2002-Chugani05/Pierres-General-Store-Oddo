<script setup>
const { id, title, imgUrl, description } = defineProps({
  id: String,
  title: String,
  imgUrl: String,
  description: String,
})
</script>

<template>
  <button
    type="button"
    :id="id"
    class="card mx-3 col-3 shadow border-dark rounded-5"
    data-bs-toggle="modal"
    :data-bs-target="'#' + id + 'Modal'"
  >
    <div class="card-body">
      <div class="row h3">
        <img class="col-1 img-fluid" :src="imgUrl" :alt="id + ' icon'" />
        {{ title }}
      </div>
      <div class="row">
        <p class="card-body text-start lead">{{ description }}</p>
      </div>
    </div>
  </button>

  <div class="modal fade" :id="id + 'Modal'" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered modal-xl">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-3" id="exampleModalLabel">
            <img :src="imgUrl" :alt="id + ' icon in modal'" class="mx-2" />
            {{ title }}
          </h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
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

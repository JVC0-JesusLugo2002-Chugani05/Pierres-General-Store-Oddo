<template>
    <button class="col create border-0 d-flex justify-content-center align-items-center display-5" data-bs-toggle="modal" data-bs-target="#createBackupModal">
        <p class="bg-light rounded w-50">Cómo crear</p>
    </button>

    <div class="modal fade" id="createBackupModal" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered modal-xl">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-3" id="createBackupModalLabel">
                        Cómo crear una copia de seguridad
                    </h1>
                    <button
                        type="button"
                        class="btn-close"
                        data-bs-dismiss="modal"
                        aria-label="Close"
                    ></button>
                </div>
                <div class="modal-body">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Reiciendis excepturi labore eligendi dolorem. Omnis ea autem doloremque aliquid accusamus, quibusdam atque illum officia reprehenderit perspiciatis fuga quas deleniti! Vero, id.
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
    background-image: url("/img/backup-section/create-background.jpeg");
}
.create:hover {
    filter: grayscale(0%);
}
</style>
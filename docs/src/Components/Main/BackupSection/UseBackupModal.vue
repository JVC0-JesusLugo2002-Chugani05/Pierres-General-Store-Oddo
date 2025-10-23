<template>
    <button class="col use border-0 d-flex justify-content-center align-items-center display-5" data-bs-toggle="modal" data-bs-target="#useBackupModal">
        <p class="bg-light rounded w-50">Cómo usar</p>
    </button>

    <div class="modal fade" id="useBackupModal" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered modal-xl">
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
                Lorem ipsum dolor sit amet consectetur, adipisicing elit. Cumque itaque eos, numquam suscipit et perspiciatis iusto magnam libero corrupti doloremque, optio voluptatibus atque molestiae deserunt modi, consectetur rerum officiis placeat.
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
    background-image: url("/img/backup-section/use-background.webp");
}
.use:hover {
    filter: grayscale(0%);
}
</style>
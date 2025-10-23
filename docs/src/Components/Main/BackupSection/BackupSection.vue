<script setup>
import Title from '../Common/Title.vue';
import CreateBackupModal from './CreateBackupModal.vue';
import UseBackupModal from './UseBackupModal.vue';
</script>

<template>
    <section id="BackupSection">
        <Title url="/img/como-usar-copias-de-seguridad.png"/>
        <div class="container mt-3">
            <div class="row">
                <CreateBackupModal/>
                <UseBackupModal/>
            </div>
        </div>
    </section>
</template>
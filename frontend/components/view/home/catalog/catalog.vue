<script setup lang="ts">
import Swiper from './swiper.vue'

const stores = setupStore('catalogList')

stores.fetchCatalogList()
</script>

<template>
  <section class="catalog">
    <h2>Каталог</h2>
    <Swiper />
  </section>
</template>

<style scoped lang="scss">
.catalog {
  display: flex;
  flex-direction: column;
  gap: 40px;
}
h2 {
  color: black;
}
</style>

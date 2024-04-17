<script setup lang="ts">
import Swiper from './swiper.vue'

const stores = setupStore(['catalogList', 'productPopList'])

await stores.catalogList.fetchCatalogList()

watch(() => stores.productPopList.catalog_id, () => {
  stores.productPopList.fetchProductPopList()
})

await stores.productPopList.fetchProductPopList()
</script>

<template>
  <section class="catalog">
    <h2>Каталог</h2>
    <Swiper />
    <h2>Популярные предложения</h2>
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

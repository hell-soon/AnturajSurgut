<script setup lang="ts">
import Swiper from './swiper.vue'
import ProductCard from './product-card.vue'

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
    <div class="product-cards">
      <ProductCard
        v-for="card in stores.productPopList.productPopList?.results"
        :key="card.product.id"
        :card="card"
      />
    </div>
  </section>
</template>

<style scoped lang="scss">
.catalog {
  display: flex;
  flex-direction: column;
  gap: 40px;
}

.product-cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  justify-content: center;
}

h2 {
  color: black;
}
</style>

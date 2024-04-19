<script setup lang="ts">
import Swiper from './swiper.vue'
import ProductCard from './product-card.vue'

const stores = setupStore(['catalogList', 'productPopList'])

await stores.catalogList.fetchCatalogList()

const visible = ref(true)

watch(() => stores.productPopList.catalog_id, () => {
  visible.value = false
  setTimeout(() => {
    visible.value = true
  }, 500)
  stores.productPopList.fetchProductPopList()
})

await stores.productPopList.fetchProductPopList()
</script>

<template>
  <section class="catalog">
    <h2>Каталог</h2>
    <Swiper />
    <h2>Популярные предложения</h2>
    <Transition name="fade">
      <div v-show="visible" class="product-cards">
        <ProductCard
          v-for="card in stores.productPopList.productPopList?.results"
          :key="card.product.id"
          :card="card"
        />
      </div>
    </Transition>
  </section>
</template>

<style scoped lang="scss">
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease-in-out;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.catalog {
  display: flex;
  flex-direction: column;
  gap: 40px;
}

.product-cards {
  grid-template-rows: 600px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  justify-content: center;
}

h2 {
  color: black;
}
</style>

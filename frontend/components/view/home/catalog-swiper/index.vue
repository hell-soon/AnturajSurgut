<script setup lang="ts">
import Swiper from './swiper.vue'
import ProductCard from './product-card.vue'

const stores = setupStore(['productPopList'])

const visible = ref(true)

watch(() => stores.productPopList.catalog_id, () => {
  visible.value = false
  setTimeout(() => {
    visible.value = true
  }, 350)

  stores.productPopList.fetchProductPopList(3)
})
</script>

<template>
  <section class="catalog">
    <h2 class="text-black">
      Каталог
    </h2>
    <Swiper />
    <!-- <h2 class="text-black">
      Популярные предложения
    </h2> -->
    <Transition name="fade">
      <div v-if="visible" class="product-cards">
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
  gap: $cover-50;
}

.product-cards {
  grid-template-rows: 600px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: $cover-50;
  justify-content: center;
}
</style>

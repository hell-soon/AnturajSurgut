<script setup lang="ts">
import Swiper from './swiper.vue'
import ProductCard from './product-card.vue'
import type { ProductParams } from '~/utils/api/service/product/product.type'

const stores = setupStore(['productList'])

const visible = ref(true)

const params: ProductParams = {
  page_size: 3,
}

watch(() => stores.productList.catalog_id, () => {
  params.catalog_id = stores.productList.catalog_id
  visible.value = false
  setTimeout(() => {
    visible.value = true
  }, 350)

  stores.productList.fetchProductList(params)
})
</script>

<template>
  <section class="catalog">
    <h2 class="text-black">
      Каталог
    </h2>
    <Swiper />
    <Transition name="fade">
      <div v-if="visible" class="product-cards">
        <ProductCard
          v-for="card in stores.productList.productList?.results"
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
  gap: clamp($cover-20, 20vw, $cover-50);
  justify-content: center;
  align-items: center;

  @media (max-width: 1024px) {
    grid-template-columns: repeat(2, 1fr);
  }

  @media (max-width: 628px) {
    grid-template-columns: repeat(1, 1fr);
  }
}
</style>

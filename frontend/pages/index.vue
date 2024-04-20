<script setup lang="ts">
import Swiper from '~/components/view/home/main-swiper/swiper.vue'

const stores = setupStore(['productPopList', 'catalogList'])

await stores.productPopList.fetchProductPopList()
await stores.catalogList.fetchCatalogList()
</script>

<template>
  <div class="container">
    <Swiper />
    <ViewHomeText />
    <ViewHomeCatalogSwiper />
    <ViewHomeTimelines />
    <ViewHomeReviews />
  </div>
</template>

<style scoped lang="scss">
.container {
  margin-top: $cover-30;
  margin-bottom: $cover-30;
  display: flex;
  flex-direction: column;
  gap: 230px;
}
</style>

<script setup lang="ts">
import Swiper from '~/components/view/home/main-swiper/swiper.vue'

const stores = setupStore(['productList', 'catalogList'])

const params = {
  catalog_id: 1,
  page_size: 3,
}

await stores.productList.fetchProductList(params)
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
  margin-bottom: $cover-60;
  display: flex;
  flex-direction: column;
  gap: 230px;
}
</style>

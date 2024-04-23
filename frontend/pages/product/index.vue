<script setup lang="ts">
const store = setupStore(['productList', 'catalogList', 'productFilters'])

watch(() => store.productList.params, (newValue) => {
  const paramsCopy = { ...newValue }
  paramsCopy.page = 1
  store.productList.fetchProductList(paramsCopy)
}, { deep: true })

store.catalogList.fetchCatalogList()
store.productList.fetchProductList()
store.productFilters.fetchProductFilters()
// if (store.productList.params)
//   store.productList.fetchProductList(store.productList.params)
</script>

<template>
  <section class="container">
    <div class="block">
      <div class="filters">
        <ViewProductsProductGridFilter />
      </div>
      <div class="card-grid">
        <ViewProductsProductGrid />
        <v-pagination
          v-if="store.productList.productList?.total_pages! > 1"
          v-model="store.productList.params.page"
          :total-visible="8"
          :length="store.productList.productList?.total_pages"
        />
      </div>
    </div>
  </section>
</template>

<style scoped lang="scss">
.container {
  margin-top: $cover-60;
  margin-bottom: $cover-60;
}

.block {
  display: grid;
  grid-template-columns: 300px 1fr;
  width: 100%;
  gap: $cover-50;
}
</style>

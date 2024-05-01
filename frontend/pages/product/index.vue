<script setup lang="ts">
const store = setupStore(['productList', 'catalogList', 'productFilters'])

store.catalogList.fetchCatalogList()
store.productFilters.fetchProductFilters()

watch(() => store.productList.params, (newValue) => {
  const paramsCopy = { ...newValue }
  store.productList.fetchProductList(paramsCopy)

  store.productList.loading = true
  setTimeout(() => {
    store.productList.loading = false
  }, 500)
}, { deep: true, immediate: true, flush: 'sync' })
</script>

<template>
  <section class="container">
    <div class="block">
      <div class="filters">
        <ViewProductsProductGridFilter />
      </div>
      <div class="card-grid">
        <ViewProductsProductGridTegsGroups />
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

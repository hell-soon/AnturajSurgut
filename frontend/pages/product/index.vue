<script setup lang="ts">
const store = setupStore(['productList', 'catalogList'])

// Используйте watch для глубокого отслеживания изменений
watch(() => store.productList.params, (newValue) => {
  // Копируйте объект, чтобы избежать мутации исходного объекта
  const paramsCopy = { ...newValue }
  // Вызовите fetchProductList с копией объекта params
  store.productList.fetchProductList(paramsCopy)
}, { deep: true })

store.catalogList.fetchCatalogList()
store.productList.fetchProductList(store.productList.params)

if (store.productList.params)
  store.productList.fetchProductList(store.productList.params)
</script>

<template>
  <section class="container">
    <!-- <h1 class="text-black">
      Список ТОваров
    </h1> -->
    <div class="d-flex block">
      <div class="filters">
        <ViewProductsProductGridFilter />
      </div>
      <div class="card-grid">
        <ViewProductsProductGrid />
        <v-pagination
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
  width: 100%;
  gap: $cover-50;
}
</style>

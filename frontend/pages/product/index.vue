<script setup lang="ts">
const store = setupStore(['productList'])

// Используйте watch для глубокого отслеживания изменений
watch(() => store.productList.params, (newValue) => {
  // Копируйте объект, чтобы избежать мутации исходного объекта
  const paramsCopy = { ...newValue }
  // Вызовите fetchProductList с копией объекта params
  store.productList.fetchProductList(paramsCopy)
}, { deep: true })

store.productList.fetchProductList()
</script>

<template>
  <div class="container">
    <h1 class="text-black">
      Список ТОваров
    </h1>
    <ViewProductsProductGrid />
  </div>
</template>

<style scoped lang="scss">
.container {
  margin-top: $cover-60;
  margin-bottom: $cover-60;
}
</style>

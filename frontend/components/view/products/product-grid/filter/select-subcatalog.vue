<script setup lang="ts">
const store = setupStore(['productList', 'catalogList'])

watch(() => store.productList.params.catalog_id, () => {
  if (store.productList.params.catalog_id) {
    store.catalogList.fetchSubcatalog(store.productList.params.catalog_id)
    store.productList.params.subcatalog_id = undefined
  }
})
</script>

<template>
  <v-select
    v-if="store.productList.params.catalog_id"
    v-model="store.productList.params.subcatalog_id"
    label="Подкаталог"
    density="comfortable"
    item-title="name"
    item-value="id"
    :items="store.catalogList.subcatalog"
    variant="underlined"
    multiple
  />
</template>

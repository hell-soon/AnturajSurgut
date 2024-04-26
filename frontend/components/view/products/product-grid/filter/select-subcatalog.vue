<script setup lang="ts">
import { watchParam } from '~/utils/helpers/filters'

const store = setupStore(['productList', 'catalogList'])

watchParam('catalog_id', 'catalog_id', (catalog_id) => {
  store.catalogList.fetchSubcatalog(catalog_id)
})

watchParam('subcatalog_id', 'subcatalog_id')
</script>

<template>
  <v-select
    v-if="store.productList.params.catalog_id"
    v-model="store.productList.params.subcatalog_id"
    clearable
    label="Подкаталог"
    density="comfortable"
    item-title="name"
    item-value="id"
    :items="store.catalogList.subcatalog"
    variant="underlined"
    chips
    multiple
  />
</template>

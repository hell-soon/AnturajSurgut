<script setup lang="ts">
import { watchParam } from '~/utils/helpers/filters'

const store = setupStore(['productList', 'catalogList'])

watchParam('catalog_id', 'catalog_id', (catalog_id: number) => {
  store.catalogList.fetchSubcatalog(catalog_id)
})

watch(() => store.productList.params.catalog_id, () => {
  store.productList.params.subcatalog_id = undefined
})

watchParam('subcatalog_id', 'subcatalog_id')
</script>

<template>
  <v-select
    v-model="store.productList.params.subcatalog_id"
    :disabled="!store.productList.params.catalog_id"
    clearable
    label="Подкаталог"
    density="comfortable"
    item-title="name"
    item-value="id"
    :items="store.catalogList.subcatalog"
    variant="underlined"
    chips
    multiple
    closable-chips
  />
</template>

<script setup lang="ts">
const store = setupStore(['productList', 'catalogList'])
</script>

<template>
  <v-select
    v-model="store.productList.params.catalog_id"
    label="Каталог"
    density="comfortable"
    item-title="name"
    item-value="id"
    :items="store.catalogList.catalogList"
    variant="underlined"
  />
</template>

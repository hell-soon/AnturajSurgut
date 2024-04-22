<script setup lang="ts">
import SelectCatalog from './select-catalog.vue'
import SelectSubcatalog from './select-subcatalog.vue'

const store = setupStore(['productList'])
</script>

<template>
  <div>
    <h1 class="text-black">
      Filters
    </h1>
    <div class="">
      <v-checkbox
        v-model="store.productList.params.high_rating"
        label="По популярности"
      />
      <SelectCatalog />
      <SelectSubcatalog />
    </div>
  </div>
</template>

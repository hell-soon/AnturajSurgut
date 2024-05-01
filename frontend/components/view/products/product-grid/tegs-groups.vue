<script setup lang="ts">
import { watchParam } from '~/utils/helpers/filters'

const store = setupStore(['productList', 'productFilters'])

store.productFilters.fetchProductTags()

watchEffect(() => {
  store.productFilters.fetchProductTags(store.productList.params.catalog_id, store.productList.params.subcatalog_id)
})
</script>

<template>
  <v-responsive class="overflow-y-auto" max-width="1000px">
    <v-chip-group
      v-model="store.productList.params.tags"
      multiple
    >
      <v-chip
        v-for="i in store.productFilters.productTags"
        :key="i.id"
        :text="i.name"
        :value="i.id"
        filter
      />
    </v-chip-group>
  </v-responsive>
</template>

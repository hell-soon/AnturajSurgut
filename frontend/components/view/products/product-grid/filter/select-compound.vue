<script setup lang="ts">
import { watchParam } from '~/utils/helpers/filters'

const store = setupStore(['productFilters', 'productList'])

watchParam('compound_id', 'compound_id')
</script>

<template>
  <v-select
    v-model="store.productList.params.compound_id"
    clearable
    label="Материал"
    item-title="name"
    item-value="id"
    :items="store.productFilters.productFilters?.compound"
    variant="underlined"
    multiple
  >
    <template #selection="{ item, index }">
      <v-chip
        v-if="index < 2"
        variant="tonal"
      >
        <span>{{ item.title }}</span>
      </v-chip>
      <span
        v-if="index === 2"
        class="text-grey text-caption align-self-center"
      >
        (+{{ store.productList.params.compound_id?.length! - 2 }} еще)
      </span>
    </template>
  </v-select>
</template>

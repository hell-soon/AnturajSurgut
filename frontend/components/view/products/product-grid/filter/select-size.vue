<script setup lang="ts">
import { watchParam } from '~/utils/helpers/filters'

const store = setupStore(['productFilters', 'productList'])

watchParam('size_id', 'size_id')
</script>

<template>
  <v-select
    v-model="store.productList.params.size_id"
    clearable
    label="Размер"
    item-title="name"
    item-value="id"
    :items="store.productFilters.productFilters?.size"
    variant="underlined"
    multiple
  >
    <template #selection="{ item, index }">
      <v-chip
        v-if="index < 4"
        variant="tonal"
      >
        <span>{{ item.title }}</span>
      </v-chip>
      <span
        v-if="index === 4"
        class="text-grey text-caption align-self-center"
      >
        (+{{ store.productList.params.size_id?.length! - 4 }} еще)
      </span>
    </template>
  </v-select>
</template>

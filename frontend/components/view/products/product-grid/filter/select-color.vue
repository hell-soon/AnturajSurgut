<script setup lang="ts">
import { watchParam } from '~/utils/helpers/filters'

const store = setupStore(['productFilters', 'productList'])

watchParam('color_id', 'color_id')
</script>

<template>
  <v-select
    v-model="store.productList.params.color_id"
    clearable
    label="Цвет"
    item-title="name"
    item-value="id"
    :items="store.productFilters.productFilters?.color"
    variant="underlined"
    multiple
    closable-chips
  >
    <template #selection="{ item, index }">
      <v-chip
        v-if="index < 2"
        :style="`background-color: ${item.raw.color}`"

        :variant="item.raw.color === '#FFFFFF' || item.raw.color === '#FFFF00' ? 'tonal' : 'flat'"
      >
        <span>{{ item.title }}</span>
      </v-chip>
      <span
        v-if="index === 2"
        class="text-grey text-caption align-self-center"
      >
        (+{{ store.productList.params.color_id?.length! - 2 }} еще)
      </span>
    </template>
  </v-select>
</template>

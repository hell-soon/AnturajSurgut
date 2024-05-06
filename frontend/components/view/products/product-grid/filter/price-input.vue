<script setup lang="ts">
const store = setupStore(['productFilters', 'productList'])

const min = ref()
const max = ref()

watch (() => store.productFilters.productFilters?.cost_range, () => {
  min.value = store.productFilters.productFilters?.cost_range.min.toString()
  max.value = store.productFilters.productFilters?.cost_range.max.toString()
})

min.value = store.productFilters.productFilters?.cost_range.min.toString()
max.value = store.productFilters.productFilters?.cost_range.max.toString()
</script>

<template>
  <v-container class="pa-0">
    <v-row no-gutters>
      <v-col cols="10">
        <v-text-field
          v-model="store.productList.params.price_min"
          clearable
          label="Цена от"
          :placeholder="`${min} руб.`"
          variant="underlined"
        />
      </v-col>
      <v-col cols="10">
        <v-text-field
          v-model="store.productList.params.price_max"
          clearable
          label="Цена до"
          :placeholder="`${max} руб.`"
          variant="underlined"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped lang="scss"></style>

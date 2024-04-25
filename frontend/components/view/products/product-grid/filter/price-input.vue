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
  <v-container>
    <span class="text-black footnote d-flex align-center justify-center">Цена</span>
    <v-row>
      <v-col>
        <v-text-field v-model="store.productList.params.price_min" clearable :placeholder="`${min} руб.`" variant="underlined" />
      </v-col>
      <v-col>
        <v-text-field v-model="store.productList.params.price_max" clearable :placeholder="`${max} руб.`" variant="underlined" />
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped lang="scss"></style>

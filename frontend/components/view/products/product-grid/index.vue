<script setup lang="ts">
import Card from './card.vue'

const store = setupStore(['productList'])
</script>

<template>
  <div>
    <h1 class="text-black">
      Product Grid
    </h1>
    <div class="">
      <Card v-for="(card, i) in store.productList.productList?.results" :key="i" :card="card" />
    </div>
    <v-pagination
      v-model="store.productList.params.page"
      :total-visible="8"
      :length="store.productList.productList?.total_pages"
    />
  </div>
</template>

<style scoped lang="scss">
</style>

<script setup lang="ts">
import Card from './card.vue'

const store = setupStore(['productList'])
</script>

<template>
  <v-container class="pa-0">
    <v-row
      v-if="store.productList.productList?.results.length"
    >
      <v-col
        v-for="(card, i) in store.productList.productList?.results"
        :key="i"
        cols="12"
        md="3"
      >
        <Card :card="card" />
      </v-col>
    </v-row>
    <v-row v-else calss="d-flex">
      <h3 class="text-black w-100 d-flex align-center justify-center">
        Товаров нет!
      </h3>
    </v-row>
  </v-container>
</template>

<style scoped lang="scss">

</style>

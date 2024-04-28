<script setup lang="ts">
import Card from './card.vue'

const store = setupStore(['productList'])
</script>

<template>
  <div>
    <v-container>
      <v-row v-if="store.productList.productList?.results.length">
        <v-col
          v-for="(card, i) in store.productList.productList?.results"
          :key="i"
          sm="3"
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
  </div>
</template>

<style scoped lang="scss">
</style>

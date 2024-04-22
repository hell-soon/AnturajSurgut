<script setup lang="ts">
import Card from './card.vue'

const store = setupStore(['productList'])
</script>

<template>
  <div>
    <h1 class="text-black">
      Product Grid
    </h1>
    <div>
      <v-container>
        <v-row>
          <v-col
            v-for="(card, i) in store.productList.productList?.results"
            :key="i"
            sm="3"
          >
            <Card :card="card" />
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<style scoped lang="scss">
</style>

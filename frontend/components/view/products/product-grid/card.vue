<script setup lang="ts">
import type { ProductResult } from '~/types/models/product'

defineProps<{ card: ProductResult }>()
</script>

<template>
  <NuxtLink
    v-if="card.product"
    :to="`/product/${card.product.id}`"
    class="card"
  >
    <div class="card-img">
      <NuxtImg class="card-img" :src="card.product.image[0].image" alt="card" />
    </div>
    <div class="card-contant">
      <span class="body text-black">
        {{ card.product.name }}
      </span>
    </div>
  </NuxtLink>
  <div v-else>
    <v-skeleton-loader
      :elevation="2"
      type="image, list-item-two-line"
      height="100%"
    />
  </div>
</template>

<style scoped lang="scss">
.card {
  height: 300px;
  width: 200px;

  &-img {
    width: 100%;
    height: 200px;
    border-radius: $cover-12;

    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
  }
}
</style>

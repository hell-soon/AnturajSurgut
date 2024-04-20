<script setup lang="ts">
import type { ProductPop } from '~/types/models/product'

defineProps<{ card: ProductPop }>()
</script>

<template>
  <NuxtLink
    :to="`/product/${card.product.id}`" class="card"
  >
    <div class="card-img">
      <NuxtImg class="card-img" :src="card.product.image[0].image" alt="card" />
    </div>
    <div class="card-contant">
      <h3 class="card-contant__title text-black">
        {{ card.product.name }}
      </h3>
      <span class="card-contant__description body text-black" v-html="card.product.description" />
    </div>
  </NuxtLink>
</template>

<style scoped lang="scss">
.card {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  border-radius: $cover-12;
  overflow: hidden;
  background-color: $color-light-white;
  transition: box-shadow 0.3s ease-in-out;

  &-img {
    width: 100%;
    height: 350px;
    object-fit: cover;

    img {
      width: 100%;
      height: 100%;
    }
  }

  &-contant {
    border-top: 0;
    border-radius: 0 0 10px 10px;
    width: 100%;
    padding: $cover-24;
    height: 100%;
    display: flex;
    gap: $cover-16;
    flex-direction: column;

    &__description {
      overflow: hidden;
      width: 100%;
      height: 100px;
      max-height: 75px;
      display: -webkit-box;
      -webkit-box-orient: vertical;
      -webkit-line-clamp: 3;
      position: relative;
    }
  }

  &:hover {
    box-shadow: 0 6px 24px 0 rgba(3, 55, 52, 0.15);

    .card-contant {
      border-color: white;
    }
  }
}
</style>

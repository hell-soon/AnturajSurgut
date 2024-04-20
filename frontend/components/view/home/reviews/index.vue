<script setup lang="ts">
import Swiper from './swiper.vue'

const reviews = ref()

reviews.value = await api.review()
</script>

<template>
  <div class="reviews">
    <h2 class="text-black">
      отзывы покупателей
    </h2>
    <div class="reviews__content">
      <Swiper :slider="reviews" />
    </div>
  </div>
</template>

<style scoped lang="scss">
.reviews {
  display: flex;
  flex-direction: column;
  gap: $cover-50;
}
</style>

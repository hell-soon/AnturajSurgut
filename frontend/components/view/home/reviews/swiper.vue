<script setup lang="ts">
import { Swiper, SwiperSlide } from 'swiper/vue'
import Slide from './slide.vue'
import type { ReviewList } from '~/types/models/review'

defineProps<{ slider: ReviewList }>()

const _swiperOptions = {
  slidesPerView: 4,

  breakpoints: {
    320: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    1024: {
      slidesPerView: 3,
    },
  },
}
</script>

<template>
  <Swiper class="swiper" :="_swiperOptions">
    <SwiperSlide v-for="(item, index) in slider.results" :key="index">
      <Slide :info="item" />
    </SwiperSlide>
  </Swiper>
</template>

<style scoped lang="scss">
.swiper {
  width: 100%;
  height: 100%;
}
</style>

<script setup lang="ts">
import { Swiper, SwiperSlide } from 'swiper/vue'
import Slide from './slide.vue'
import type { ReviewList } from '~/types/models/review'

defineProps<{ slider: ReviewList }>()

const _swiperOptions = {
  slidesPerView: 4,
}
</script>

<template>
  <Swiper :="_swiperOptions">
    <SwiperSlide v-for="(item, index) in slider.results" :key="index">
      <Slide :info="item" />
    </SwiperSlide>
  </Swiper>
</template>

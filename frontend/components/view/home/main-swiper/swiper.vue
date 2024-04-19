<script setup lang="ts">
import { Swiper, SwiperSlide } from 'swiper/vue'
import { Autoplay, EffectCreative } from 'swiper/modules'
import Slide from './slide.vue'

const _swiperOptions = {
  modules: [EffectCreative, Autoplay],
  autoplay: { delay: 10000, pauseOnMouseEnter: true },
  slidesPerView: 1,
  loop: true,
  creativeEffect: {
    prev: {
      translate: [0, 0, -400],
    },
    next: {
      translate: ['100%', 0, 0],
    },
  },
  effect: 'creative',
  centeredSlides: true,
}

const slider = ref()

slider.value = await api.slider()
</script>

<template>
  <div>
    <Swiper :="_swiperOptions">
      <SwiperSlide v-for="item in slider" :key="item.id">
        <Slide :slide="item" />
      </SwiperSlide>
    </Swiper>
  </div>
</template>

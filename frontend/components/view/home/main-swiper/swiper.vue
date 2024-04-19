<script setup lang="ts">
import { Autoplay, EffectCreative } from 'swiper/modules'
import type { SwiperOptions } from 'swiper/types'
import { register } from 'swiper/element-bundle'
import Slide from './slide.vue'

const _swiperOptions: SwiperOptions = {
  modules: [EffectCreative, Autoplay],
  autoplay: { delay: 10000, pauseOnMouseEnter: true },
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

await api.slider().then((res) => {
  slider.value = res
})

register()
</script>

<template>
  <swiper-container :="_swiperOptions">
    <swiper-slide v-for="item in slider" :key="item.id">
      <Slide :slide="item" />
    </swiper-slide>
  </swiper-container>
</template>

<script setup lang="ts">
import 'swiper/element/css/scrollbar'
import 'swiper/element/css/autoplay'

import { Autoplay, EffectCreative } from 'swiper/modules'
import type { SwiperOptions } from 'swiper/types'
import { register } from 'swiper/element-bundle'
import Slide from './slide.vue'

const _swiperOptions: SwiperOptions = {
  modules: [EffectCreative, Autoplay],
  autoplay: { delay: 10000, pauseOnMouseEnter: true },
  autoHeight: true,
  loop: true,
  effect: 'creative',
  creativeEffect: {
    prev: {
      translate: [0, 0, -400],
    },
    next: {
      translate: ['100%', 0, 0],
    },
  },
}

register()

const slider = ref()

api.slider().then((res) => {
  slider.value = res
})
</script>

<template>
  <div class="container">
    <swiper-container :="_swiperOptions">
      <swiper-slide v-for="item in slider" :key="item.id">
        <Slide :slide="item" />
      </swiper-slide>
    </swiper-container>
  </div>
</template>

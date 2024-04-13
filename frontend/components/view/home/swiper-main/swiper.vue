<script setup lang="ts">
import { Swiper, SwiperSlide } from 'swiper/vue'
import { Autoplay, EffectFade, Scrollbar } from 'swiper/modules'
import type { SwiperOptions } from 'swiper/types'
import Slid from './slide.vue'

import 'swiper/scss'
import 'swiper/scss/effect-fade'
import 'swiper/scss/scrollbar'

const swiperOptions = {
  modules: [EffectFade, Scrollbar, Autoplay],
  scrollbar: { hide: true },
  autoplay: { delay: 5000 },
  loop: true,
  effect: 'fade',
} as SwiperOptions
</script>

<template>
  <div style="width: 100%">
    <Swiper :options="swiperOptions" class="swiper">
      <SwiperSlide>
        <Slid>
          <img src="https://swiperjs.com/demos/images/nature-1.jpg" alt="">
        </Slid>
      </SwiperSlide>
      <SwiperSlide>
        <Slid>
          <img src="https://swiperjs.com/demos/images/nature-2.jpg" alt="">
        </Slid>
      </SwiperSlide>
    </Swiper>
  </div>
</template>

<style scoped lang="scss">
</style>

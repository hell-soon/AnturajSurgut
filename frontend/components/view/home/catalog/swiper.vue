<script setup lang="ts">
import 'swiper/element/css/autoplay'

import { Autoplay, EffectCoverflow } from 'swiper/modules'
import type { Swiper, SwiperEvents, SwiperOptions } from 'swiper/types'
import { register } from 'swiper/element-bundle'

const _swiperOptions: SwiperOptions = {
  modules: [EffectCoverflow, Autoplay],
  loop: true,
  autoplay: { delay: 20000, pauseOnMouseEnter: true },
  coverflowEffect: {
    rotate: 50,
    depth: 100,
    stretch: 0,
    scale: 0.7,
  },
  slidesPerView: 3,
  effect: 'coverflow',
}

register()

function onSlideChange(e: any) {
  // eslint-disable-next-line no-console
  console.log('slide changed', e.detail[0].realIndex)
}

const stores = setupStore('catalogList')
</script>

<template>
  <swiper-container :="_swiperOptions" @swiperslidechange-transitionstart="onSlideChange">
    <swiper-slide
      v-for="item in stores.catalogList"
      :key="item.id"
      class="slide"
    >
      <img v-if="item.image" :src="item.image">
      <h3>{{ item.name }}</h3>
    </swiper-slide>
  </swiper-container>
</template>

<style scoped lang="scss">
.slide {
  position: relative;
  width: 400px;
  height: 450px;
  border-radius: 10px;
  overflow: hidden;

  img {
    filter: brightness(60%);
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
  }

  h3 {
    position: absolute;
    text-align: center;
    top: 50%;
    transform: translateY(-50%) translateX(-50%);
    left: 50%;
    z-index: 20;
  }
}
</style>

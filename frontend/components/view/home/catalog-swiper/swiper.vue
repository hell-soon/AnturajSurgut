<script setup lang="ts">
import { Autoplay, EffectCoverflow } from 'swiper/modules'
import type { SwiperOptions } from 'swiper/types'
import { register } from 'swiper/element-bundle'

const stores = setupStore(['productPopList', 'catalogList'])

const _swiperOptions: SwiperOptions = {
  modules: [EffectCoverflow, Autoplay],
  autoplay: { delay: 20000, pauseOnMouseEnter: true },
  loop: true,
  coverflowEffect: {
    rotate: 50,
    depth: 100,
    stretch: 0,
    scale: 0.7,
  },
  slidesPerView: 3,
  effect: 'coverflow',
  centeredSlides: true,
}

register()

function onSlideChange(e: any) {
  const a = (e.detail[0].realIndex + 1) as number
  stores.productPopList.catalog_id = a
}
</script>

<template>
  <swiper-container :="_swiperOptions" @swiperslidechange="onSlideChange">
    <swiper-slide
      v-for="item in stores.catalogList.catalogList"
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

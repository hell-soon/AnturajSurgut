<script setup lang="ts">
import { Swiper, SwiperSlide } from 'swiper/vue'
import { Autoplay, EffectCoverflow } from 'swiper/modules'

const stores = setupStore(['productList', 'catalogList'])

const _swiperOptions = {
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

function onSlideChange(e: any) {
  const a = (e.realIndex + 1) as number
  stores.productList.catalog_id = a
}
</script>

<template>
  <div>
    <Swiper :="_swiperOptions" @slide-change="onSlideChange">
      <SwiperSlide
        v-for="item in stores.catalogList.catalogList"
        :key="item.id"
        class="slide"
      >
        <img v-if="item.image" :src="item.image">
        <h3>{{ item.name }}</h3>
      </SwiperSlide>
    </Swiper>
  </div>
</template>

<style scoped lang="scss">
.slide {
  position: relative;
  width: 400px;
  height: 450px;
  border-radius: $cover-12;
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

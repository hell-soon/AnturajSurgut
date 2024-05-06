<script setup lang="ts">
import { useDisplay } from 'vuetify'
import Button from '~/components/shared/button.vue'
import type { ButtonType } from '~/components/shared/button.vue'
import type { SiteSliderResponse } from '~/utils/api/service/slider/slider.type'

const props = defineProps<{ slide: SiteSliderResponse }>()

const { sm, xs } = useDisplay()

const button: ButtonType = {
  link: props.slide.url,
  text: 'Подробнее',
}
</script>

<template>
  <div
    class="slide" :style="{
      background: sm || xs ? `linear-gradient(180deg, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.2) 100%),
      url(${slide.image})` : ``,
      backgroundSize: 'cover',
      backgroundPosition: 'center' }"
  >
    <div class="slide-text d-flex flex-column">
      <p class="text-h4" :style="{ color: sm || xs ? 'white' : '' }" v-html="slide.text" />
      <Button :item="button" />
    </div>
    <div class="slide-img">
      <img :src="slide.image">
    </div>
  </div>
</template>

<style scoped lang="scss">
.slide {
  background-color: $color-white;
  position: relative;
  justify-content: space-between;
  display: flex;
  height: 600px;
  border-radius: 10px;
  overflow: hidden;
  align-items: center;

  &-img {
    padding: $cover-30;
    width: 1000px;
    height: 100%;

    img {
      border-radius: 10px;
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
  }

  &-text {
    max-width: 400px;
    height: 100%;
    justify-content: space-around;
    padding: $cover-30;
  }

  @media (max-width: 1024px) {
    &-img {
      display: none;
    }
  }
}
</style>

<script setup lang="ts">
import Button from '~/components/shared/button.vue'
import type { ButtonType } from '~/components/shared/button.vue'
import type { SiteSliderResponse } from '~/utils/api/service/slider/slider.type'

const props = defineProps<{ slide: SiteSliderResponse }>()

const button: ButtonType = {
  link: props.slide.url,
  text: 'Подробнее',
}
</script>

<template>
  <div class="slide">
    <div class="slide-text d-flex flex-column">
      <p class="text-h4" v-html="slide.text" />
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
}
</style>

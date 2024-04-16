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
    <img :src="slide.image">
    <div class="slide-text d-flex flex-column">
      <h1>{{ slide.text }}</h1>
      <Button :item="button" />
    </div>
  </div>
</template>

<style scoped lang="scss">
.slide {
  position: relative;
  height: 85vh;
  border-radius: 10px;
  overflow: hidden;

  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  &-text {
    position: absolute;
    top: 35%;
    left: 10%;
    gap: 50px;

    h1 {
      color: $color-white;
    }
  }
}
</style>

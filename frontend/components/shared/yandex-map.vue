<script setup lang="ts">
import {
  YandexMap,
  YandexMapControlButton,
  YandexMapControls,
  YandexMapDefaultFeaturesLayer,
  YandexMapDefaultSchemeLayer,
  YandexMapMarker,
  YandexMapZoomControl,
} from 'vue-yandex-maps'
import type { LngLat } from '@yandex/ymaps3-types'
import type { Address } from '~/types/models/contact'

const props = defineProps<{ address?: Address }>()

const center = ref([props.address?.longitude, props.address?.latitude] as LngLat)

function openYandexMaps() {
  const url = `https://yandex.ru/maps/?&ll=${props.address?.longitude},${props.address?.latitude}&text=${encodeURIComponent('Антураж')}&z=16`
  window.open(url, '_blank')
}
</script>

<template>
  <div class="map">
    <div class="map-container">
      <YandexMap
        :settings="{
          location: {
            center: center as LngLat,
            zoom: 15,
          },
          zoomRange: {
            min: 12,
            max: 20,
          },
        }"
        theme
        height="100%"
        width="100%"
      >
        <YandexMapDefaultSchemeLayer :settings="{ theme: 'light' }" />
        <YandexMapDefaultFeaturesLayer />
        <YandexMapControls :settings="{ position: 'right' }">
          <YandexMapZoomControl />
        </YandexMapControls>
        <YandexMapControls :settings="{ position: 'bottom left' }">
          <YandexMapControlButton>
            <div class="open-maps-button" @click="openYandexMaps">
              Открыть Яндекс Карты
            </div>
          </YandexMapControlButton>
        </YandexMapControls>
        <YandexMapMarker
          :settings="{
            coordinates: center as LngLat,
          }"
          position="top left-center"
        >
          <img class="pin" src="/img/shared/pin.png" alt="pin">
        </YandexMapMarker>
      </YandexMap>
    </div>
  </div>
</template>

<style scoped lang="scss">
.pin {
  display: block;
  margin: auto;
}

.open-maps-button {
  align-items: center;
  display: flex;
  font-size: 12px;
  justify-content: center;

  &::before {
    background-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBkPSJNMTIgMWE5LjAwMiA5LjAwMiAwIDAgMC02LjM2NiAxNS4zNjJjMS42MyAxLjYzIDUuNDY2IDMuOTg4IDUuNjkzIDYuNDY1LjAzNC4zNy4zMDMuNjczLjY3My42NzMuMzcgMCAuNjQtLjMwMy42NzMtLjY3My4yMjctMi40NzcgNC4wNi00LjgzMSA1LjY4OS02LjQ2QTkuMDAyIDkuMDAyIDAgMCAwIDEyIDF6bTAgMTIuMDc5YTMuMDc5IDMuMDc5IDAgMSAxIDAtNi4xNTggMy4wNzkgMy4wNzkgMCAwIDEgMCA2LjE1OHoiIGZpbGw9IiNGNDMiLz48L3N2Zz4=);
    background-size: 14px 14px;
    content: '';
    display: inline-block;
    height: 14px;
    margin-right: 6px;
    width: 14px;
  }
}

.map {
  display: flex;
  flex-direction: column;
  gap: clamp(24px, 5vw, 32px);

  &-container {
    overflow: hidden;
    border-radius: 15px;
    width: 100%;
    height: clamp(222px, 30vw, 492px);
  }
}
</style>

<script setup lang="ts">
import Swiper from '~/components/view/home/swiper-main/swiper.vue'
</script>

<template>
  <v-app>
    <div class="container">
      <Swiper />
      <ViewHomeText />
    </div>
  </v-app>
</template>

<style scoped lang="scss">
.container {
  margin-top: $cover-30;
  display: flex;
  flex-direction: column;
  gap: 230px;
}
</style>

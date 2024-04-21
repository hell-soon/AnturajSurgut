<script setup lang="ts">
import Modal from '../shared/modal.vue'
import List from '~/utils/mock/header-list'
</script>

<template>
  <header>
    <div class="container link-hover">
      <div class="logo">
        <nuxt-link to="/">
          <NuxtImg
            width="200"
            height="25"
            src="/logo.svg"
          />
        </nuxt-link>
      </div>
      <div class="list">
        <nuxt-link
          v-for="(item, index) in List.main"
          :key="index"
          class="footnote"
          :to="item.link"
        >
          {{ item.name }}
        </nuxt-link>
      </div>

      <div class="list">
        <Modal
          v-for="(item, index) in List.second"
          :key="index"
          :to="item.link"
        >
          <template #activator>
            <v-badge :color="item.badge ? '#e6e4e1' : 'transparent'" dot>
              <img :src="`/icons/${item.name}.svg`" :alt="item.name">
            </v-badge>
          </template>
        </Modal>
      </div>
    </div>
  </header>
</template>

<style scoped lang="scss">
header {
  z-index: 2;
  position: relative;
  background: url('/img/header/green-texture.jpg');
  box-shadow: $shadow-main;
}

.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 0 20px 0;
}

.list {
  display: flex;
  gap: 55px;
  justify-content: center;
}
</style>

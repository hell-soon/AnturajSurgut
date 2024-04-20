<script setup lang="ts">
interface ListItem {
  name: string
  link?: string
}

const listMain: ListItem[] = [
  {
    name: 'Товары',
    link: '/product',
  },
  {
    name: 'Услуги',
    link: '/services',
  },
  {
    name: 'Оптовикам',
    link: '/wholesalers',
  },
  {
    name: 'О нас',
    link: '/about',
  },
]

const listSecond: ListItem[] = [
  {
    name: 'profile',
    link: '/profile',
  },
  {
    name: 'search',
  },
  {
    name: 'shopping-cart',
  },
]
</script>

<template>
  <header>
    <div class="container link-hover">
      <div class="list">
        <nuxt-link
          v-for="(item, index) in listMain"
          :key="index"
          class="footnote"
          :to="item.link"
        >
          {{ item.name }}
        </nuxt-link>
      </div>
      <div class="logo">
        <nuxt-link to="/">
          <NuxtImg
            width="200"
            height="47"
            src="/logo.svg"
          />
        </nuxt-link>
      </div>
      <div class="list">
        <nuxt-link
          v-for="(item, index) in listSecond"
          :key="index"
          :to="item.link"
        >
          <img :src="`/icons/${item.name}.svg`" alt="phone">
        </nuxt-link>
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

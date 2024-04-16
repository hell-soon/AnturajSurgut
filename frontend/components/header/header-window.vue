<script setup lang="ts">
interface ListItem {
  name: string
  link?: string
}

const listMain: ListItem[] = [
  {
    name: 'Товары',
    link: '/products',
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
    <div class="container">
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

  box-shadow: 2px 2px 2px 1px rgba(0, 0, 0, 0.2);
}

.footnote {
  transition: text-shadow 0.3s ease-in-out;
  &:hover {
    text-shadow: 6px 6px 6px rgba(0, 0, 0, 0.5);
  }
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

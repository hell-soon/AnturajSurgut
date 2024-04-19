<script setup lang="ts">
import Map from '../shared/yandex-map.vue'

const about = [
  {
    name: 'О нас',
    link: '/about',
  },
  {
    name: 'Контакты',
    link: '/contact',
  },
  {
    name: 'Вакансии',
    link: '/vacancy',
  },
]

const clients = [
  {
    name: 'Покупателям',
  },
  {
    name: 'Доставка и оплата',
    link: '/delivery-payment',
  },
  {
    name: 'Обмен и возврат',
    link: '/exchange-refund',
  },
  {
    name: 'Дисконтная программа',
    link: '/discount-program',
  },
  {
    name: 'Способы оплаты',
    link: '/sposoby-oplaty',
  },
]
</script>

<template>
  <footer>
    <div class="container">
      <div class="nav">
        <div class="nav-list">
          <div class="nav-list__block">
            <nuxt-link
              v-for="(item, index) in about"
              :key="index"
              :class="[index === 0 ? 'h2' : 'footnote']"
              :to="item.link"
            >
              {{ item.name }}
            </nuxt-link>
          </div>
          <div class="nav-list__block">
            <nuxt-link
              v-for="(item, index) in clients"
              :key="index"
              :class="[index === 0 ? 'h2' : 'footnote']"
              :to="item.link"
            >
              {{ item.name }}
            </nuxt-link>
          </div>
        </div>
        <div class="nav-map">
          <Map />
        </div>
        <div class="nav-info" />
      </div>
    </div>
  </footer>
</template>

<style scoped lang="scss">
footer {
  margin-top: auto;
  z-index: 2;
  position: relative;
  background: url('/img/header/green-texture.jpg');
  box-shadow: -2px -2px 2px 1px rgba(0, 0, 0, 0.2);
  padding-top: 30px;

  padding-bottom: 30px;

  &::before {
    content: '';
    width: 100%;
    position: absolute;
    top: 1rem;
    left: 0;
    height: 5px;
    border-top: 2px dashed #fff;
  }

  .nav {
    display: flex;
    justify-content: space-between;
    width: 100%;

    &-list {
      display: flex;
      flex-direction: column;
      gap: 20px;
      flex-wrap: wrap;

      &__block {
        display: flex;
        flex-direction: column;
        gap: 10px;

        .h2 {
          padding-bottom: 5px;
        }
      }
    }

    &-map {
      width: 600px;
    }
  }
}
</style>

<script setup lang="ts">
import { useDisplay } from 'vuetify'
import Map from '../shared/yandex-map.vue'

const { sm, xs } = useDisplay()

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

const store = setupStore(['contactList'])
await store.contactList.fetchContactList(false, true)
const data = store.contactList.contactList
</script>

<template>
  <footer>
    <div v-if="!sm && !xs" class="container link-hover">
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
          <Map :address="data?.address" />
        </div>
        <div class="nav-info">
          <SharedSocialLink :info="data?.contact.phone!" params="tel" />
          <SharedSocialLink :info="data?.contact.email!" params="mailto" />
          <div class="nav-info__social">
            <span class="body">Мы в соцсетях</span>
            <div class="nav-info__social-icons">
              <a
                v-for="(item, index) in data?.social_accounts"
                :key="index"
                :href="item.url"
                target="_blank"
              >
                <img :src="item.icon">
              </a>
            </div>
          </div>
        </div>
      </div>
      <div class="dop-info">
        <span class="footnote">«Антураж», 2006-2024</span>
        <NuxtLink to="/privacy-policy" class="footnote">
          Политика конфиденциальности
        </nuxtlink>
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
  box-shadow: $shadow-reverse;
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

  .container {
    display: flex;
    gap: 20px;
    flex-direction: column;
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

    &-info {
      display: flex;
      flex-direction: column;
      gap: 30px;

      &__social {
        display: flex;
        flex-direction: column;
        gap: 10px;

        &-icons {
          display: flex;
          flex-wrap: wrap;
          gap: 20px;

          a {
            height: 35px;

            img {
              width: 100%;
              height: 100%;
              object-fit: cover;
            }
          }
        }
      }
    }
  }

  .dop-info {
    display: flex;
    width: 100%;
    justify-content: space-between;
  }
}
</style>

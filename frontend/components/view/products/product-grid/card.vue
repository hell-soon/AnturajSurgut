<script setup lang="ts">
import type { ProductResult } from '~/types/models/product'

defineProps<{ card: ProductResult }>()

const store = setupStore(['productList'])

const heart = ref(false)

function favorite(id: number) {
  heart.value = !heart.value

  if (localStorage.getItem('product')) {
    const arr = JSON.parse(localStorage.getItem('product')!)

    if (arr.includes(id.toString()))
      arr.splice(arr.indexOf(id.toString()), 1)
    else
      arr.push(id.toString())

    localStorage.setItem('product', JSON.stringify(arr))
  }
  else {
    localStorage.setItem('product', JSON.stringify([id.toString()]))
  }
}
</script>

<template>
  <div
    v-if="store.productList.loading === false && card.product"
    class="card d-flex flex-column ga-2"
  >
    <NuxtLink
      :to="`/product/${card.product.id}`"
    >
      <div class="card-img">
        <NuxtImg
          v-if="card.product.image[0].image"
          class="card-img"
          :src="card.product.image[0].image"
          alt="card"
        />
        <v-skeleton-loader
          v-else
          type="image"
        />
      </div>
      <div class="card-contant">
        <div class="card-contant__title">
          <span class="body text-black">
            {{ card.product.name }}
          </span>
        </div>
        <div class="card-contant__description">
          <v-chip variant="tonal" size="small" color="#138f87">
            {{ card.product.tags[0].name }}
          </v-chip>
        </div>
      </div>
    </NuxtLink>

    <div class="card-contant__footer">
      <div class="d-flex align-center ">
        <span class="footnote text-grey-darken-1">
          {{ card.product.min_cost }} ₽
        </span>
        <v-spacer />
        <v-btn
          icon
          variant="text"
          size="small"
          :color="heart ? 'red' : 'grey-darken-3'"
          @click="favorite(card.product.id)"
        >
          <v-icon>mdi-heart</v-icon>
        </v-btn>
        <v-btn icon variant="text" size="small" color="grey-darken-3">
          <v-icon>mdi-cart</v-icon>
        </v-btn>
      </div>
    </div>
  </div>
  <div v-else>
    <v-skeleton-loader
      class="card"
      type="image, list-item-two-line, button, avatar, avatar"
      height="380px"
    />
  </div>
</template>

<style scoped lang="scss">
.card {
  height: 400px;
  max-width: 100%;
  justify-content: space-between;

  &-img {
    width: 100%;
    height: 250px;
    border-radius: $cover-12;

    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
  }

  &-contant {
    display: flex;
    gap: $cover-16;
    flex-direction: column;
  }
}
</style>

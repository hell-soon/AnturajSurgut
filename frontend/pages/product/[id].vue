<script setup lang="ts">
import { useRoute } from 'vue-router'
import type { ProductResult } from '~/types/models/product'

const store = setupStore(['productInfo'])
const route = useRoute()

const product = ref() as Ref<ProductResult | null>

watchEffect(() => {
  product.value = store.productInfo.product
})

store.productInfo.fetchProductInfo(Number(route.params.id))
</script>

<template>
  <div class="container">
    <div class="fixed">
      <div class="fixed-lift">
        <v-carousel
          v-if="product?.product.image"
          show-arrows="hover"
          height="900px"
          hide-delimiter-background
          class="sticky"
        >
          <v-carousel-item
            v-for="(slide, i) in product?.product.image"
            :key="i"
            :src="slide.image"
            :lazy-src="slide.image"
            cover
          />
        </v-carousel>
      </div>
      <div>
        <view-products-product-info :product="product" />
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.container {
  margin: $cover-60 auto;
  height: 100%;
}

.fixed {
  display: grid;
  grid-template-columns: 600px 1fr;
  gap: $cover-20;
  height: 100%;

  &-lift {
    height: 100%;

    .sticky {
      position: sticky;
      top: 10px;
    }
  }
}
</style>

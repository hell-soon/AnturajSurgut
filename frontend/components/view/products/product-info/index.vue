<script setup lang="ts">
import type { ProductResult } from '~/types/models/product'

const props = defineProps<{ product: ProductResult | null }>()

const colorActive = ref(0)
const sizeActive = ref(0)
const sizes = ref()
function colorSelect(id: number) {
  colorActive.value = id
  sizeActive.value = 0
  sizes.value = props.product?.product_info?.info[id].sizes
}

function sizeSelect(id: number) {
  sizeActive.value = id
}
</script>

<template>
  <div class="block">
    <h1 class="text-black">
      {{ product?.product.name }}
    </h1>
    <div class="group">
      <v-chip
        v-for="i in product?.product.tags"
        :key="i.id"
      >
        {{ i.name }}
      </v-chip>
    </div>
    <div class="color">
      <h3 class="text-black">
        Цвета
      </h3>
      <div class="group">
        <v-btn
          v-for="(ietm, i) in product?.product_info?.info"
          :key="ietm.color.id"
          icon
          variant="flat"
          :color="ietm.color.color"
          :class="colorActive === i ? 'active' : ''"
          @click="colorSelect(i)"
        />
      </div>
    </div>

    <div class="size">
      <h3 class="text-black">
        Размер
      </h3>
      <div class="group">
        <v-btn
          v-for="(item, i) in sizes"
          :key="i"
          variant="flat"
          :class="sizeActive === i ? 'active' : ''"
          @click="sizeSelect(i)"
        >
          {{ item.size.name }}
        </v-btn>
      </div>
    </div>

    <div class="description">
      <p class="text-black body">
        {{ product?.product.description }}
      </p>
    </div>
    <div class="price">
      <h3 class="text-black">
        {{ product?.product_info?.info[colorActive].sizes[sizeActive].cost }} ₽
      </h3>
    </div>
  </div>
</template>

<style scoped lang="scss">
.block {
  display: flex;
  flex-direction: column;
  align-items: end;
  text-align: end;
  gap: $cover-20;
}

.active {
  filter: brightness(0.2);
}

.color-btn {
  border: 2px;
}
</style>

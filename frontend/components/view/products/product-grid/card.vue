<script setup lang="ts">
import type { ProductResult } from '~/types/models/product'

defineProps<{ card: ProductResult }>()
</script>

<template>
  <div>
    {{ card.product.name }}
  </div>
</template>

<style scoped lang="scss">
</style>

<script setup lang="ts">
import SelectCatalog from './select-catalog.vue'
import SelectSubcatalog from './select-subcatalog.vue'
import SelectColor from './select-color.vue'
import SelectSize from './select-size.vue'
import SelectCompound from './select-compound.vue'
import PriceInpuit from './price-input.vue'

import type { ProductParams } from '~/utils/api/service/product/product.type'

const url = useRequestURL()
const router = useRouter()

const store = setupStore(['productList'])

function watchParam(paramName: string, storeKey: keyof ProductParams) {
  watch(() => store.productList.params[storeKey], (newValue) => {
    const url = useRequestURL()

    if (newValue)
      url.searchParams.append(paramName, 'true')
    else
      url.searchParams.delete(paramName)

    router.push(url.pathname + url.search)
  })

  if (url.searchParams.has(paramName))
    store.productList.params[storeKey] = true as unknown as undefined // Set to true explicitly
  else
    store.productList.params[storeKey] = undefined // Set to undefined explicitly
}

// Использование функции для каждого параметра
watchParam('high_rating', 'high_rating')
watchParam('most_sold', 'most_sold')

function Clear() {
  store.productList.params = {}
  router.push(url.pathname)
}
</script>

<template>
  <div>
    <h1 class="text-black">
      Filters
    </h1>
    <div class="filter-block">
      <PriceInpuit />
      <v-checkbox
        v-model="store.productList.params.high_rating"
        label="По популярности"
      />
      <v-checkbox
        v-model="store.productList.params.most_sold"
        label="Самые продаваемые"
      />
      <SelectCatalog />
      <SelectSubcatalog />
      <SelectColor />
      <SelectSize />
      <SelectCompound />
    </div>
    <v-btn @click="Clear">
      Очистить
    </v-btn>
  </div>
</template>

<style scoped lang="scss">
.filter-block {
  width: 100%;
}
</style>

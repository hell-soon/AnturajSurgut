<script setup lang="ts">
import SelectCatalog from './select-catalog.vue'
import SelectSubcatalog from './select-subcatalog.vue'
import SelectColor from './select-color.vue'
import SelectSize from './select-size.vue'
import SelectCompound from './select-compound.vue'
import PriceInpuit from './price-input.vue'

const url = useRequestURL()
const router = useRouter()

const store = setupStore(['productList'])

watch(() => store.productList.params.high_rating, () => {
  const url = useRequestURL()

  if (store.productList.params.high_rating)
    url.searchParams.append('high_rating', 'true')
  else
    url.searchParams.delete('high_rating')

  router.push(url.pathname + url.search)
})

if (url.searchParams.has('high_rating'))
  store.productList.params.high_rating = true
else
  store.productList.params.high_rating = undefined

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

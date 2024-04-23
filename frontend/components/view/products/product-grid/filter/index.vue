<script setup lang="ts">
import SelectCatalog from './select-catalog.vue'
import SelectSubcatalog from './select-subcatalog.vue'

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
    <div class="">
      <v-checkbox
        v-model="store.productList.params.high_rating"
        label="По популярности"
      />
      <SelectCatalog />
      <SelectSubcatalog />
    </div>
    <v-btn @click="Clear">
      Очистить
    </v-btn>
  </div>
</template>

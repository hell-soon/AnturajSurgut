<script setup lang="ts">
import type { ProductParams } from '~/utils/api/service/product/product.type'

const store = setupStore(['productList', 'catalogList'])

const url = useRequestURL()
const router = useRouter()

// Функция для создания наблюдателя параметров
function watchParam(
  paramName: string,
  storeKey: keyof ProductParams,
  fetchData?: (value: number) => void,
) {
  watch(() => store.productList.params[storeKey], (newValue) => {
    const url = useRequestURL()

    if (newValue) {
      const serializedValue = JSON.stringify(newValue)
      url.searchParams.set(paramName, serializedValue)
    }
    else {
      url.searchParams.delete(paramName)
    }

    router.push(url.pathname + url.search)
  })

  if (url.searchParams.has(paramName)) {
    const deserializedValue = JSON.parse(url.searchParams.get(paramName)!)
    store.productList.params[storeKey] = deserializedValue
  }
  else {
    store.productList.params[storeKey] = undefined
  }

  if (fetchData && store.productList.params[storeKey])
    fetchData(store.productList.params[storeKey] as number)
}

watchParam('catalog_id', 'catalog_id', (catalogId) => {
  store.catalogList.fetchSubcatalog(catalogId)
})

watchParam('subcatalog_id', 'subcatalog_id')
</script>

<template>
  <v-select
    v-if="store.productList.params.catalog_id"
    v-model="store.productList.params.subcatalog_id"
    clearable
    label="Подкаталог"
    density="comfortable"
    item-title="name"
    item-value="id"
    :items="store.catalogList.subcatalog"
    variant="underlined"
    chips
    multiple
  />
</template>

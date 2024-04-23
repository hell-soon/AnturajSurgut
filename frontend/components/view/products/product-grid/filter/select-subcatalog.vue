<script setup lang="ts">
const store = setupStore(['productList', 'catalogList'])

// const url = useRequestURL()
const router = useRouter()

watch(() => store.productList.params.catalog_id, () => {
  store.productList.params.subcatalog_id = undefined
  if (store.productList.params.catalog_id)
    store.catalogList.fetchSubcatalog(store.productList.params.catalog_id)
})

watch(() => store.productList.params.subcatalog_id, () => {
  const url = useRequestURL()

  if (store.productList.params.subcatalog_id) {
    const subcatalogArray = store.productList.params.subcatalog_id

    if (url.searchParams.has('subcatalog')) {
      const serializedSubcatalog = JSON.stringify(subcatalogArray)
      url.searchParams.set('subcatalog', serializedSubcatalog)
    }

    else {
      const serializedSubcatalog = JSON.stringify(subcatalogArray)
      url.searchParams.append('subcatalog', serializedSubcatalog)
    }
  }
  else {
    url.searchParams.delete('subcatalog')
  }

  router.push(url.pathname + url.search)
})

// if (url.searchParams.has('subcatalog'))
//   store.productList.params.subcatalog_id = Number.parseInt(url.searchParams.get('subcatalog_id')!)
// else
//   store.productList.params.subcatalog_id = undefined
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

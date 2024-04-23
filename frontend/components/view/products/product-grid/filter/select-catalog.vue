<script setup lang="ts">
const router = useRouter()
const url = useRequestURL()

const store = setupStore(['productList', 'catalogList'])

watch(() => store.productList.params.catalog_id, () => {
  const url = useRequestURL()

  if (store.productList.params.catalog_id) {
    if (url.searchParams.has('catalog'))
      url.searchParams.set('catalog', store.productList.params.catalog_id.toString())
    else
      url.searchParams.append('catalog', store.productList.params.catalog_id.toString())
  }
  else { url.searchParams.delete('catalog') }

  router.push(url.pathname + url.search)
})

if (url.searchParams.has('catalog'))
  store.productList.params.catalog_id = Number.parseInt(url.searchParams.get('catalog')!)
else
  store.productList.params.catalog_id = undefined
</script>

<template>
  <v-select
    v-model="store.productList.params.catalog_id"
    clearable
    label="Каталог"
    density="comfortable"
    item-title="name"
    item-value="id"
    :items="store.catalogList.catalogList"
    variant="underlined"
  />
</template>

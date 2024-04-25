import type { ProductParams } from '~/utils/api/service/product/product.type'

const store = setupStore(['productFilters', 'productList'])

const router = useRouter()
const url = useRequestURL()

export function watchParam(paramName: string, storeKey: keyof ProductParams) {
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
    const deserializedValue = JSON.parse(url.searchParams.get('size_id')!)
    store.productList.params[storeKey] = deserializedValue
  }
  else {
    store.productList.params[storeKey] = undefined
  }
}

import type { ProductParams } from '~/utils/api/service/product/product.type'

export function watchParam(
  paramName: string,
  storeKey: keyof ProductParams,
  fetchData?: (value: number) => void,
) {
  const store = setupStore(['productFilters', 'productList'])

  const router = useRouter()
  const url = useRequestURL()

  watch(() => store.productList.params[storeKey], (newValue) => {
    const url = useRequestURL()
    if (newValue) {
      const serializedValue = JSON.stringify(newValue)
      url.searchParams.set(paramName, serializedValue)
    }
    else {
      url.searchParams.delete(paramName)
    }

    if (fetchData && store.productList.params[storeKey])
      fetchData(store.productList.params[storeKey] as number)

    router.push(url.pathname + url.search)
  })

  if (url.searchParams.has(paramName)) {
    const deserializedValue = JSON.parse(url.searchParams.get(paramName)!)
    store.productList.params[storeKey] = deserializedValue
  }
}

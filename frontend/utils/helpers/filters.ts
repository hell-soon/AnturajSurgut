import type { ProductParams } from '~/utils/api/service/product/product.type'

export function watchParam(
  paramName: string,
  storeKey: keyof ProductParams,
  fetchData?: (value: number) => void,
  // paramValue?: boolean,

) {
  const store = setupStore(['productFilters', 'productList'])

  const router = useRouter()
  const url = useRequestURL()

  watch(() => store.productList.params[storeKey], (newValue) => {
    const url = useRequestURL()
    if (newValue) {
      // if (paramName === 'high_rating' || 'most_sold')
      //   url.searchParams.set(paramName, paramValue.toString())

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
    if (paramName === 'high_rating' || 'most_sold') {
      store.productList.params[storeKey] = true as unknown as undefined
    }
    else {
      const deserializedValue = JSON.parse(url.searchParams.get(paramName)!)
      store.productList.params[storeKey] = deserializedValue
    }
  }

  if (fetchData && store.productList.params[storeKey])
    fetchData(store.productList.params[storeKey] as number)
}

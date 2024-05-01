import { useGlobalStore } from './common/global.store'
import { useCatalogListStore } from './module/home/catalog-list.store'
import { useProductListStore } from './module/home/product-list.store'
import { useContactListStore } from './module/shared/contact.store'
import { useProductFilterstStore } from './module/shared/product-filters.store'

type ExtractStoreId<T> = T extends { $id: infer U } ? U : never

interface IStoreTypes {
  global: ReturnType<typeof useGlobalStore>
  catalogList: ReturnType<typeof useCatalogListStore>
  productList: ReturnType<typeof useProductListStore>
  contactList: ReturnType<typeof useContactListStore>
  productFilters: ReturnType<typeof useProductFilterstStore>
}

type StoreKeys = ExtractStoreId<IStoreTypes[keyof IStoreTypes]>

export const stores: Readonly<{ [K in StoreKeys]: () => IStoreTypes[K] }> = Object.freeze({
  global: useGlobalStore,
  catalogList: useCatalogListStore,
  productList: useProductListStore,
  contactList: useContactListStore,
  productFilters: useProductFilterstStore,
})

function setupStore<T extends StoreKeys>(key: T): Readonly<IStoreTypes[T]>
function setupStore<T extends StoreKeys>(keys: T[]): Readonly<{ [K in T]: IStoreTypes[K]; }>
function setupStore<T extends StoreKeys>(keysOrKey: T[] | T) {
  if (Array.isArray(keysOrKey))
    return Object.fromEntries(keysOrKey.map(key => [key, stores[key]()])) as { [K in T]: IStoreTypes[K] }

  return stores[keysOrKey]()
}

export { setupStore }

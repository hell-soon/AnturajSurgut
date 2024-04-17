import type { ProductPopList } from '~/types/models/product'

//* --- State ----------------------------------------------- *//
interface ProductPopListState {
  productPopList: ProductPopList | null
  catalog_id: number
  error: unknown
}

//* --- Store ----------------------------------------------- *//
export const useProductPopListStore = defineStore('productPopList', {
  state: (): ProductPopListState => ({
    productPopList: null,
    catalog_id: 1,
    error: {},
  }),

  actions: {
    async fetchProductPopList() {
      await api.productPop(this.catalog_id)
        .then((res) => {
          this.productPopList = res
        })
        .catch((err) => {
          this.error = err
        })
    },
  },
})

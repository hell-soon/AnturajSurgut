import type { ProductPopList } from '~/types/models/product'

//* --- State ----------------------------------------------- *//
interface ProductPopListState {
  productPopList: ProductPopList | null
  catalog_id: number
  page_size: number
  error: unknown
}

//* --- Store ----------------------------------------------- *//
export const useProductPopListStore = defineStore('productPopList', {
  state: (): ProductPopListState => ({
    productPopList: null,
    catalog_id: 1,
    page_size: 3,
    error: {},
  }),

  actions: {
    async fetchProductPopList() {
      try {
        const res = await api.productPop(this.catalog_id, this.page_size)
        this.productPopList = res
      }
      catch (err) {
        this.error = err
      }
    },
  },
})

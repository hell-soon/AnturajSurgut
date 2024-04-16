import type { ProductPopListResponse } from '~/utils/api/service/product/product.type'

//* --- State ----------------------------------------------- *//
interface ProductPopListState {
  productPopList: ProductPopListResponse[]
  error: unknown
}

//* --- Store ----------------------------------------------- *//
export const useProductPopListStore = defineStore('productPopList', {
  state: (): ProductPopListState => ({
    productPopList: [],
    error: {},
  }),

  actions: {
    async fetchProductPopList() {
      await api.productPop()
        .then((res) => {
          this.productPopList = res
        })
        .catch((err) => {
          this.error = err
        })
    },
  },
})

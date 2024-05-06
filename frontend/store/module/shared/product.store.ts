import type { ProductResult } from '~/types/models/product'

//* --- State ----------------------------------------------- *//
interface ProductInfoState {
  product: ProductResult | null
  error: unknown
}

//* --- Store ----------------------------------------------- *//
export const useProductInfoStore = defineStore('productInfo', {
  state: (): ProductInfoState => ({
    product: null,
    error: null,
  }),

  actions: {
    async fetchProductInfo(id: number) {
      try {
        const res = await api.productInfo(id)
        this.product = res
      }
      catch (err) {
        this.error = err
      }
    },
  },
})

import type { ProductFilters } from '~/types/models/product-filters'

//* --- State ----------------------------------------------- *//
interface ProductFiltersState {
  productFilters: ProductFilters | null
  error: unknown
}

//* --- Store ----------------------------------------------- *//
export const useProductFilterstStore = defineStore('productFilters', {
  state: (): ProductFiltersState => ({
    productFilters: null,
    error: {},
  }),

  actions: {
    async fetchProductFilters() {
      try {
        const res = await api.filter()
        this.productFilters = res
      }
      catch (err) {
        this.error = err
      }
    },
  },
})

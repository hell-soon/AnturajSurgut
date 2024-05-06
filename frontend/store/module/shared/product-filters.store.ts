import type { ProductFilters } from '~/types/models/product-filters'
import type { ProductTag } from '~/types/models/product-tags'

//* --- State ----------------------------------------------- *//
interface ProductFiltersState {
  productFilters: ProductFilters | null
  productTags: ProductTag[] | null
  error: unknown
}

//* --- Store ----------------------------------------------- *//
export const useProductFilterstStore = defineStore('productFilters', {
  state: (): ProductFiltersState => ({
    productFilters: null,
    productTags: null,
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

    async fetchProductTags(catalog_id?: number, subcatalog_id?: number[]) {
      try {
        const res = await api.tags(catalog_id, subcatalog_id)
        this.productTags = res.results
      }
      catch (err) {
        this.error = err
      }
    },
  },
})

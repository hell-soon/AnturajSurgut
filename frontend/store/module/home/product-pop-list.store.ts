import type { ProductList } from '~/types/models/product'
import type { ProductParams } from '~/utils/api/service/product/product.type'

//* --- State ----------------------------------------------- *//
interface ProductListState {
  productList: ProductList | null
  catalog_id: number
  params: ProductParams
  error: unknown
}

//* --- Store ----------------------------------------------- *//
export const useProductListStore = defineStore('productList', {
  state: (): ProductListState => ({
    productList: null,
    catalog_id: 1,
    params: {},
    error: null,
  }),

  actions: {
    async fetchProductList(params?: ProductParams) {
      try {
        const res = await api.product(params)
        this.productList = res
      }
      catch (err) {
        this.error = err
        this.params.page = 1
      }
    },
  },
})

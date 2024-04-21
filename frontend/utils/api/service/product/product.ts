import type { ProductParams } from './product.type'
import type { ProductList as ProductListResponse } from '~/types/models/product'

export function getProductList(params?: ProductParams) {
  return getReq<ProductListResponse>('/list/product/', params)
}

import type { ProductResponse } from './product.type'

export function getProductList(headers?: any) {
  return getReq<ProductResponse>('/list/product', headers)
}

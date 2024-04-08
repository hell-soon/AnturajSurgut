import type { ProductResponse } from './product.type'

export function getProductList(headers?: any) {
  getReq<ProductResponse>('/fact', headers)
}

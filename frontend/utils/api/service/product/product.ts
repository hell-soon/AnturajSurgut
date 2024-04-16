import type { ProductPopListResponse } from './product.type'

export function getProductPopList() {
  return getReq<ProductPopListResponse[]>('')
}

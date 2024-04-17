import type { ProductPopList as ProductPopListResponse } from '~/types/models/product'

export function getProductPopList(catalog_id: number) {
  return getReq<ProductPopListResponse>('/list/product/', { catalog_id })
}

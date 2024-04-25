import type { ProductFilters as ProductFiltersResponse } from '~/types/models/product-filters'

export function getProductFilterList() {
  return getReq<ProductFiltersResponse>('/product/filters/')
}

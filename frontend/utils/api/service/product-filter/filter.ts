import type { ProductFilters as ProductFiltersResponse } from '~/types/models/product-filters'
import type { ProductTags as ProductTagsResponse } from '~/types/models/product-tags'

export function getProductFilterList() {
  return getReq<ProductFiltersResponse>('/product/filters/')
}

export function getProductTagsList(catalog_id?: number, subcatalog_id?: number[]) {
  return getReq<ProductTagsResponse>('/product/tags/', { catalog_id, subcatalog_id })
}

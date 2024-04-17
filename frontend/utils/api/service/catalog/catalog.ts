import type { Catalog as CatalogResponse } from '~/types/models/catalog'

export function getCatalogList() {
  return getReq<CatalogResponse[]>('/list/catalog')
}

import type { CatalogResponse } from './catalog.type'

export function getCatalogList() {
  return getReq<CatalogResponse[]>('/list/catalog')
}

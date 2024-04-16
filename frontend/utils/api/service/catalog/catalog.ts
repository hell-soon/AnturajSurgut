import type { CatalogResponse } from '../../../../types/models/catalog.type'

export function getCatalogList() {
  return getReq<CatalogResponse>('/list/catalog')
}

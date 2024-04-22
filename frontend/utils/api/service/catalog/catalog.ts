import type {
  Catalog as CatalogResponse,
  SubCatalog as SubCatalogResponse,
} from '~/types/models/catalog'

export function getCatalogList() {
  return getReq<CatalogResponse[]>('/list/catalog')
}

export function getSubcatalog(catalog_id: number) {
  return getReq<SubCatalogResponse[]>('/list/subcatalog', { catalog_id })
}

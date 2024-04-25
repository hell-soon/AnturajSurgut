import type {
  Catalog as CatalogResponse,
  SubCatalog as SubCatalogResponse,
} from '~/types/models/catalog'

export function getCatalogList() {
  return getReq<CatalogResponse[]>('/product/catalog/')
}

export function getSubcatalog(catalog_id: number) {
  return getReq<SubCatalogResponse[]>('/product/subcatalog/', { catalog_id })
}

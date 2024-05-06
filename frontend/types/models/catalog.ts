export interface Catalog {
  id: number
  name: string
  image: string
  subcatalog?: SubCatalog
}

export interface SubCatalog {
  id: number
  name: string
  image: string
}

import type { Catalog } from './catalog'

export interface ProductList {
  count: number
  next?: string
  previous?: string
  total_pages: number
  results: ProductResult[]
}

export interface ProductResult {
  catalog: Catalog
  product: Product
}

export interface Product {
  id: number
  name: string
  description: string
  image: ProductImage[]
  tags: TagsProduct[]
  compound: CompoundList[]
  rating: number
}

export interface CompoundList {
  id: number
  name: string
}

export interface ProductImage {
  image: string
}

export interface TagsProduct {
  id: number
  name: string
}

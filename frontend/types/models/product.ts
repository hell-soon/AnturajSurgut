import type { Catalog } from './catalog'

export interface ProductPopList {
  count: number
  next?: string
  previous?: string
  total_pages: number
  results: ProductPop[]
}

export interface ProductPop {
  catalog: Catalog
  product: Product
}

export interface Product {
  id: number
  name: string
  description: string
  image: ProductImage[]
  tags: TagsProduct[]
}

export interface ProductImage {
  image: string
}

export interface TagsProduct {
  id: number
  name: string
}

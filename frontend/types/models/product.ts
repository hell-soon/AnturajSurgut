import type { Catalog } from './catalog'

export interface ProductPopList {
  count: number
  next?: string
  previous?: string
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
  image: string[]
  tags: TagsProduct[]
}

export interface TagsProduct {
  id: number
  name: string
}

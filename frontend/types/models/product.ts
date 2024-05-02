import type { Catalog } from './catalog'
import type { ProductColor, ProductFIlterItem } from './product-filters'

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
  product_info?: ProductInfo
}

export interface Product {
  id: number
  name: string
  description: string
  image: ProductImage[]
  tags: TagsProduct[]
  compound: CompoundList[]
  min_cost: number
  // rating: number
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

export interface ProductInfo {
  info: Info[]
}

interface Info {
  color: ProductColor
  sizes: ProductInfoSize[]
}

interface ProductInfoSize {
  size: ProductFIlterItem
  cost: number
  promotion: boolean
  promotion_cost?: number
  quantity: number
}

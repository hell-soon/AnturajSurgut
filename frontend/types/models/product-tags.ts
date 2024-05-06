export interface ProductTags {
  count: number
  next?: string
  previous?: string
  results: ProductTag[]
}

export interface ProductTag {
  id: number
  name: string
}

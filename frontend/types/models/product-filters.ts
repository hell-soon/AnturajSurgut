export interface ProductFilters {
  color: ProductColor[]
  size: ProductFIlterItem[]
  compound: ProductFIlterItem[]
  cost_range: ProductCostRange
}

export interface ProductColor {
  id: number
  name: string
  color: string
}

export interface ProductFIlterItem {
  id: number
  name: string
}

interface ProductCostRange {
  min: number
  max: number
}

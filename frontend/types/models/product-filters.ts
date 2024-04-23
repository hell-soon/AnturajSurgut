export interface ProductFilters {
  color: ProductColor[]
  size: ProductFIlterItem[]
  compound: ProductFIlterItem[]
  cost_range: ProductCostRange
}

interface ProductColor {
  id: number
  name: string
  color: string
}

interface ProductFIlterItem {
  id: number
  name: string
}

interface ProductCostRange {
  min: number
  max: number
}

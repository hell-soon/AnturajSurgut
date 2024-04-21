export interface ProductParams {
  tags?: number[]
  create_at?: Date
  high_rating?: boolean
  catalog_id?: number
  subcatalog_id?: number[]
  compound_id?: number[]
  price_min?: number
  price_max?: number
  color_id?: number[]
  size_id?: number[]
  page?: number
  page_size?: number
}

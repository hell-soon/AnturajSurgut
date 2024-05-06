import type { ProductParams } from './product.type'
import type {
  ProductResult as ProductInfoResponse,
  ProductList as ProductListResponse,
} from '~/types/models/product'

export function getProductList(params?: ProductParams) {
  return getReq<ProductListResponse>('/product/list/', params)
}

export function getProductInfo(id: number) {
  return getReq<ProductInfoResponse>(`/product/list/${id}/`)
}

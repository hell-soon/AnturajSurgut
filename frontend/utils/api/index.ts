import { getCatalogList, getSubcatalog } from './service/catalog/catalog'
import { getContactList } from './service/contact/contact'
import { getProductFilterList, getProductTagsList } from './service/product-filter/filter'
import { getProductInfo, getProductList } from './service/product/product'
import { postProfileAuth } from './service/profile/profile'
import { getReviewList } from './service/review/review'
import { getSiteSliderList } from './service/slider/slider'

export const api = {
  slider: getSiteSliderList,
  catalog: getCatalogList,
  subcatalog: getSubcatalog,
  product: getProductList,
  productInfo: getProductInfo,
  filter: getProductFilterList,
  tags: getProductTagsList,
  contact: getContactList,
  review: getReviewList,
  auth: postProfileAuth,
}

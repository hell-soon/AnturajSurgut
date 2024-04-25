import { getCatalogList, getSubcatalog } from './service/catalog/catalog'
import { getContactList } from './service/contact/contact'
import { getProductFilterList } from './service/product-filter/filter'
import { getProductList } from './service/product/product'
import { postProfileAuth } from './service/profile/profile'
import { getReviewList } from './service/review/review'
import { getSiteSliderList } from './service/slider/slider'

export const api = {
  slider: getSiteSliderList,
  catalog: getCatalogList,
  subcatalog: getSubcatalog,
  product: getProductList,
  filter: getProductFilterList,
  contact: getContactList,
  review: getReviewList,
  auth: postProfileAuth,
}

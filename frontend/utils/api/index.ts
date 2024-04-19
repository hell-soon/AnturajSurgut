import { getCatalogList } from './service/catalog/catalog'
import { getContactList } from './service/contact/contact'
import { getProductPopList } from './service/product/product'
import { getSiteSliderList } from './service/slider/slider'

export const api = {
  slider: getSiteSliderList,
  catalog: getCatalogList,
  productPop: getProductPopList,
  contact: getContactList,
}

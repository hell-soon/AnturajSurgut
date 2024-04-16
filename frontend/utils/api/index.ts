import { getCatalogList } from './service/catalog/catalog'
import { getSiteSliderList } from './service/slider/slider'

export const api = {
  slider: getSiteSliderList,
  catalog: getCatalogList,
}

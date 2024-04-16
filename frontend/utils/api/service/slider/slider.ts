import type { SiteSliderResponse } from './slider.type'

export function getSiteSliderList() {
  return getReq<SiteSliderResponse>('/site/slider')
}

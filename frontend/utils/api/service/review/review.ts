import type { ReviewList as ReviewListResponse } from '~/types/models/review'

export function getReviewList() {
  return getReq<ReviewListResponse>('/reviews/list', { page_size: 10 })
}

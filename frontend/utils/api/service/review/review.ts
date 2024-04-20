import type { ReviewList as ReviewListResponse } from '~/types/models/review'

export function getReviewList() {
  return getReq<ReviewListResponse>('/review/review')
}

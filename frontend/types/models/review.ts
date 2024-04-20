export interface ReviewList {
  count: number
  next?: string
  previous?: string
  total_pages: number
  results: Review[]
}

export interface Review {
  user: User
  text: string
  raiting: number
  created_at: string
}

export interface User {
  first_name: string
  last_name: string
}

import type { Token as TokenReuqest } from '~/types/models/profile'

export function postProfileAuth(email: string, password: string) {
  return postReq<TokenReuqest>('/auth/login/', { email, password })
}

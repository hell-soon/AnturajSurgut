import type { ContactList as ContactResponse } from '~/types/models/contact'

export function getContactList(full_info?: boolean, include_social?: boolean) {
  return getReq<ContactResponse>('/site/contact', { full_info, include_social })
}

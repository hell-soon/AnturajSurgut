export interface ContactList {
  contact: Contact
  requisites?: Requisites
  address?: Address
  work_time?: WorkTime
  social_accounts?: SocialAccounts[]
}

export interface Contact {
  phone: string
  fax: string
  email: string
}

export interface Requisites {
  ip: string
  inn: string
  legal_address: string
}

export interface Address {
  address: string
  longitude: number
  latitude: number
}

export interface WorkTime {
  work_time: string
}

export interface SocialAccounts {
  name: string
  url: string
  icon: string
}

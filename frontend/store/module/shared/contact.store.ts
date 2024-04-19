import type { ContactList } from '~/types/models/contact'

//* --- State ----------------------------------------------- *//
interface ContactState {
  contactList: ContactList | null
  error: unknown
}

//* --- Store ----------------------------------------------- *//
export const useContactListStore = defineStore('contactList', {
  state: (): ContactState => ({
    contactList: null,
    error: {},
  }),

  actions: {
    async fetchContactList(full_info?: boolean, include_social?: boolean) {
      await api.contact(full_info, include_social)
        .then((res) => {
          this.contactList = res
        })
        .catch((err) => {
          this.error = err
        })
    },
  },
})

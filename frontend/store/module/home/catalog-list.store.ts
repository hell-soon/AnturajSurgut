import type { Catalog } from '~/types/models/catalog'

//* --- State ----------------------------------------------- *//
interface CatalogListState {
  catalogList: Catalog[]
  error: unknown
}

//* --- Store ----------------------------------------------- *//
export const useCatalogListStore = defineStore('catalogList', {
  state: (): CatalogListState => ({
    catalogList: [],
    error: {},
  }),

  actions: {
    async fetchCatalogList() {
      try {
        const res = await api.catalog()
        this.catalogList = res
      }
      catch (err) {
        this.error = err
      }
    },
  },
})

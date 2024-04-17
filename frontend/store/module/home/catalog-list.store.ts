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
      await api.catalog()
        .then((res) => {
          this.catalogList = res
        })
        .catch((err) => {
          this.error = err
        })
    },
  },
})

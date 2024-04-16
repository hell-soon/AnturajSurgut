import type { CatalogResponse } from '~/utils/api/service/catalog/catalog.type'

//* --- State ----------------------------------------------- *//
interface CatalogListState {
  catalogList: CatalogResponse[]
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

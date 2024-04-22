import type { Catalog, SubCatalog } from '~/types/models/catalog'

//* --- State ----------------------------------------------- *//
interface CatalogListState {
  catalogList: Catalog[]
  error: unknown

  subcatalog: SubCatalog[]
}

//* --- Store ----------------------------------------------- *//
export const useCatalogListStore = defineStore('catalogList', {
  state: (): CatalogListState => ({
    catalogList: [],
    error: {},
    subcatalog: [],
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

    async fetchSubcatalog(catalog_id: number) {
      try {
        const res = await api.subcatalog(catalog_id)
        this.subcatalog = res
      }
      catch (err) {
        this.error = err
      }
    },
  },
})

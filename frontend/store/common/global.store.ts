//* --- State ----------------------------------------------- *//
interface IGlobalState {
  loading: boolean
}

//* --- Store ----------------------------------------------- *//
export const useGlobalStore = defineStore('global', {
  state: (): IGlobalState => ({
    loading: true,
  }),

  actions: {
    setLoading(display: boolean) {
      this.loading = display
    },
  },
})

axios.create({
  baseURL: import.meta.env.NUXT_API_URL,
})

export const api = {
  stocks: SctocksApi(),
}

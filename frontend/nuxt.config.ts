// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: {
    enabled: true,
  },
  modules: [
    "@pinia/nuxt",  
    '@nuxt/eslint',
  ],
  imports: {
    autoImport: true,
  },

  eslint: {
    config: {
      standalone: false,
    },
  },
})

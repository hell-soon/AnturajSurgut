// https://nuxt.com/docs/api/configuration/nuxt-config
import vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'

export default defineNuxtConfig({
  devtools: {
    enabled: true,
  },
  modules: ['@pinia/nuxt', '@nuxt/image', (_options, nuxt) => {
    nuxt.hooks.hook('vite:extendConfig', (config) => {
      // @ts-expect-error: Explanation of why the error is necessary
      config.plugins.push(vuetify({ autoImport: true }))
    })
  }],
  imports: {
    autoImport: true,
  },
  build: {
    transpile: ['vuetify'],
  },
  vite: {
    vue: {
      template: {
        transformAssetUrls,
      },
    },
  },
  css: ['@/assets/scss/global.scss', '@/assets/scss/_variables.scss'],
})

// https://nuxt.com/docs/api/configuration/nuxt-config
import vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'

export default defineNuxtConfig({
  devtools: {
    enabled: true,
  },
  modules: ['@pinia/nuxt', '@nuxt/image', 'vue-yandex-maps/nuxt', (_options, nuxt) => {
    nuxt.hooks.hook('vite:extendConfig', (config) => {
      // @ts-expect-error: Explanation of why the error is necessary
      config.plugins.push(vuetify({ autoImport: true }))
    })
  }],
  imports: {
    autoImport: true,
    dirs: ['./utils/', './utils/api', './store/'],
  },
  yandexMaps: {
    apikey: 'd17123bd-3142-47c8-9496-8cb21e6d450f',
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
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: '@import "~/assets/scss/_variables.scss";',
        },
      },
    },
  },
  css: ['~/assets/scss/global.scss'],
})

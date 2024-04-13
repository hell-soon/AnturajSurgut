// https://nuxt.com/docs/api/configuration/nuxt-config
import vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'

export default defineNuxtConfig({
  devtools: {
    enabled: true,
  },
  modules: ['@pinia/nuxt', '@nuxt/image', 'nuxt-swiper', (_options, nuxt) => {
    nuxt.hooks.hook('vite:extendConfig', (config) => {
      // @ts-expect-error: Explanation of why the error is necessary
      config.plugins.push(vuetify({ autoImport: true }))
    })
  }],
  imports: {
    autoImport: true,
    dirs: ['./utils/', './utils/api'],
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

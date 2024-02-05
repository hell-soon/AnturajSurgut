import { URL, fileURLToPath } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '#': fileURLToPath(new URL('./src', import.meta.url)),
    },
    extensions: ['.js', '.json', '.jsx', '.mjs', '.ts', '.tsx', '.vue', '.store'],
  },
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `
            @import './src/assets/scss/_variables.scss';
          `,
      },
    },
  },
})

/// <reference types="vite/client" />
/// <reference types="vite-svg-loader" />

interface ImportMetaEnv {
  VITE_API_URL: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}

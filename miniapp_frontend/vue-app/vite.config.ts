import { fileURLToPath, URL } from "node:url"

import { defineConfig, loadEnv } from "vite"
import vue from "@vitejs/plugin-vue"
import vueDevTools from "vite-plugin-vue-devtools"

export default defineConfig({
    plugins: [
        vue(),
        vueDevTools(),
    ],
    resolve: {
        alias: {
            "@": fileURLToPath(new URL("./src", import.meta.url)),
            "#": fileURLToPath(new URL(".", import.meta.url))
        },
    }
})
export default defineNuxtConfig({
  devtools: { enabled: true },
  runtimeConfig: {
    API_URL: "http://127.0.0.1:8000/api/v1",
    public: {
      API_URL: "http://127.0.0.1:8000/api/v1"
    }
  },
  css: ["~/assets/css/main.css"],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  modules: [
    "@pinia/nuxt",
    [
      "@nuxtjs/google-fonts",
      {
        families: {
          Poppins: true,
        },
      },
    ],
  ],
});

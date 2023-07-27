import { defineStore } from "pinia";

interface UserPayloadInterface {
  username: string;
  password: string;
}

export const useAuthStore = defineStore("auth", {
  state: () => ({
    authenticated: false,
    loading: false,
  }),
  actions: {
    async authenticateUser({ username, password }: UserPayloadInterface) {
      // useFetch from nuxt 3
      const { data, pending }: any = await useFetch(
        "http://127.0.0.1:8000/api/v1/auth/login/",
        {
          method: "post",
          mode: "cors",
          headers: {
            "Content-Type": "application/json",
          },
          body: {
            username: username,
            password: password,
          },
        }
      );
      this.loading = pending;

      if (data.value) {
        const token = useCookie("token"); // useCookie new hook in nuxt 3
        token.value = data?.value?.token; // set token to cookie
        this.authenticated = true; // set authenticated  state value to true
      }
    },
    logUserOut() {
      const token = useCookie("token"); // useCookie new hook in nuxt 3
      this.authenticated = false; // set authenticated  state value to false
      token.value = null; // clear the token cookie
    },
  },
});

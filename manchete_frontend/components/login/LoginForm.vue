<template>
  <div class="flex justify-center flex-1">
    <div class="w-full sm:w-5/6 md:w-4/6 lg:w-1/2 xl:w-5/12 p-6 flex flex-col">
      <div class="flex flex-row items-center justify-center py-8 px-3">
        <LogoTitle />
      </div>
      <div class="flex flex-col items-start justify-center grow pb-20">
        <div class="w-full p-6 space-y-4 md:space-y-6 sm:p-8">
          <h1
            class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-3xl dark:text-white"
          >
            Acesse sua conta
          </h1>
          <div>
            <form
              v-if="!isAuthLoading"
              class="space-y-4 md:space-y-6"
              action="#"
            >
              <div>
                <label
                  for="email"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Email</label
                >
                <input
                  v-model="user.username"
                  type="email"
                  name="email"
                  id="email"
                  class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="Digite seu email"
                  required="true"
                />
              </div>
              <div>
                <label
                  for="password"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Senha</label
                >
                <input
                  v-model="user.password"
                  type="password"
                  name="password"
                  id="password"
                  placeholder="••••••••"
                  class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"
                  required="true"
                />
              </div>
              <button
                @click.prevent="login"
                class="w-full text-white bg-indigo-600 hover:bg-indigo-600 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center"
              >
                Entrar
              </button>
            </form>
            <div
              v-else
              class="w-full h-[228px] flex flex-col items-center justify-center"
            >
              <div class="text-center">
                <Loading />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="flex-1 bg-indigo-300 text-center hidden lg:flex">
      <div
        class="m-12 xl:m-16 w-full bg-contain bg-center bg-no-repeat"
        style="
          background-image: url('../assets/images/undraw_content_re_33px.svg');
        "
      ></div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const isAuthLoading = ref(false);
const user = ref({
  username: "",
  password: "",
});

function authorize() {
  isAuthLoading.value = true;

  setTimeout(() => {
    isAuthLoading.value = false;
  }, 3000);
}

const login = async () => {
  // TODO send user Data to the login endpoint and redirect if  successful
};
</script>
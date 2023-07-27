<script setup>
import { storeToRefs } from "pinia";
import { useAuthStore } from "../store/auth";
import { ref } from "vue";

definePageMeta({
  layout: "default",
});

const router = useRouter();

const { authenticateUser } = useAuthStore();
const { authenticated } = storeToRefs(useAuthStore());
const token = useCookie("token");

if (!authenticated) {
  router.push("/");
}

const isLoading = ref(true);
const newsBody = ref({
  title: "",
  subtitle: "",
  body: "",
});

setTimeout(() => {
  isLoading.value = false;
}, 2000);

const sendSubmission = async () => {
  console.log(token.value);
  if (
    newsBody.value.title.length > 0 &&
    newsBody.value.subtitle.length > 0 &&
    newsBody.value.body.length > 0
  ) {
    isLoading.value = true;
    const { data, pending } = await useFetch(
      "http://127.0.0.1:8000/api/v1/news/",
      {
        method: "post",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${token.value}`,
        },
        body: {
          title: newsBody.value.title,
          subtitle: newsBody.value.subtitle,
          body: newsBody.value.body,
        },
        onResponse({ request, response, options }) {
          isLoading.value = false;
        },
        onResponseError({ request, response, options }) {
          console.log("Erro");
          console.log(response.status);
          isLoading.value = false;
        },
      }
    );
  } else {
    console.log("lançar alert");
  }
};

const updateBody = (value) => {
  newsBody.value.body = value;
};
</script>

<template>
  <div>
    <div class="max-w-screen-xl px-6 pt-4 mx-auto">
      <form>
        <div class="space-y-12">
          <div class="border-b border-gray-900/10 pb-12">
            <div v-if="!isLoading">
              <h2 class="text-base font-semibold leading-7 text-gray-900">
                Notícia
              </h2>
              <p class="mt-1 text-sm leading-6 text-gray-600">
                Crie uma nova notícia para os leitores.
              </p>
            </div>
            <!-- Skeleton -->
            <div v-else class="animate-pulse" role="status">
              <div class="justify-start mt-6">
                <div
                  class="h-[35px] bg-gray-300 max-w-[135px] mb-2.5 rounded-md mt-1"
                ></div>
                <div
                  class="h-[30px] bg-gray-300 max-w-[320px] mb-2.5 rounded-md"
                ></div>
              </div>
            </div>

            <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
              <div class="sm:col-span-4">
                <div v-if="!isLoading">
                  <label
                    for="username"
                    class="block text-sm font-medium leading-6 text-gray-900"
                    >Título</label
                  >
                  <div class="mt-2">
                    <div
                      class="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md"
                    >
                      <input
                        v-model="newsBody.title"
                        type="text"
                        name="news-title"
                        id="news-title"
                        autocomplete="news-title"
                        class="block flex-1 border-0 bg-transparent py-1.5 px-1 text-gray-900 placeholder:text-gray-400 focus:outline-none sm:text-sm sm:leading-6"
                      />
                    </div>
                  </div>
                </div>
                <!-- Skeleton -->
                <div v-else class="animate-pulse" role="status">
                  <div class="justify-start mt-6">
                    <div
                      class="h-[30px] bg-gray-300 max-w-[135px] mb-2.5 rounded-md mt-1"
                    ></div>
                    <div
                      class="h-[45px] bg-gray-300 max-w-[455px] mb-2.5 rounded-md"
                    ></div>
                  </div>
                </div>
              </div>

              <div class="sm:col-span-4">
                <div v-if="!isLoading">
                  <label
                    for="username"
                    class="block text-sm font-medium leading-6 text-gray-900"
                    >Subtítulo</label
                  >
                  <div class="mt-2">
                    <div
                      class="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md"
                    >
                      <input
                        v-model="newsBody.subtitle"
                        type="text"
                        name="news-subtitle"
                        id="news-subtitle"
                        autocomplete="news-subtitle"
                        class="block flex-1 border-0 bg-transparent py-1.5 px-1 text-gray-900 placeholder:text-gray-400 focus:outline-none sm:text-sm sm:leading-6"
                      />
                    </div>
                  </div>
                </div>
                <!-- Skeleton -->
                <div v-else class="animate-pulse" role="status">
                  <div class="justify-start mt-6">
                    <div
                      class="h-[30px] bg-gray-300 max-w-[135px] mb-2.5 rounded-md mt-1"
                    ></div>
                    <div
                      class="h-[45px] bg-gray-300 max-w-[455px] mb-2.5 rounded-md"
                    ></div>
                  </div>
                </div>
              </div>

              <div class="col-span-full">
                <div v-if="!isLoading">
                  <label
                    for="about"
                    class="block text-sm font-medium leading-6 text-gray-900"
                    >Corpo da notícia</label
                  >
                  <div class="mt-2">
                    <div class="">
                      <client-only>
                        <NewsCreatorEditor @updateBody="updateBody" />
                      </client-only>
                    </div>
                  </div>
                </div>
                <!-- Skeleton -->
                <div v-else class="animate-pulse" role="status">
                  <div class="justify-start mt-6">
                    <div
                      class="h-[30px] bg-gray-300 max-w-[135px] mb-2.5 rounded-md mt-1"
                    ></div>
                    <div
                      class="h-[150px] bg-gray-300 max-w-[1230px] mb-2.5 rounded-md"
                    ></div>
                  </div>
                </div>
              </div>

              <!-- <div class="col-span-full">
                <div v-if="!isLoading">
                  <label
                    for="cover-photo"
                    class="block text-sm font-medium leading-6 text-gray-900"
                    >Foto principal</label
                  >
                  <div
                    class="mt-2 flex justify-center rounded-lg border border-dashed border-gray-900/25 px-6 py-10"
                  >
                    <div class="text-center">
                      <svg
                        class="mx-auto h-12 w-12 text-gray-300"
                        viewBox="0 0 24 24"
                        fill="currentColor"
                        aria-hidden="true"
                      >
                        <path
                          fill-rule="evenodd"
                          d="M1.5 6a2.25 2.25 0 012.25-2.25h16.5A2.25 2.25 0 0122.5 6v12a2.25 2.25 0 01-2.25 2.25H3.75A2.25 2.25 0 011.5 18V6zM3 16.06V18c0 .414.336.75.75.75h16.5A.75.75 0 0021 18v-1.94l-2.69-2.689a1.5 1.5 0 00-2.12 0l-.88.879.97.97a.75.75 0 11-1.06 1.06l-5.16-5.159a1.5 1.5 0 00-2.12 0L3 16.061zm10.125-7.81a1.125 1.125 0 112.25 0 1.125 1.125 0 01-2.25 0z"
                          clip-rule="evenodd"
                        />
                      </svg>
                      <div class="mt-4 flex text-sm leading-6 text-gray-600">
                        <label
                          for="file-upload"
                          class="relative cursor-pointer rounded-md bg-white font-semibold text-indigo-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-indigo-600 focus-within:ring-offset-2 hover:text-indigo-500"
                        >
                          <span>Upload a file</span>
                          <input
                            id="file-upload"
                            name="file-upload"
                            type="file"
                            class="sr-only"
                          />
                        </label>
                        <p class="pl-1">or drag and drop</p>
                      </div>
                      <p class="text-xs leading-5 text-gray-600">
                        PNG, JPG, GIF up to 10MB
                      </p>
                    </div>
                  </div>
                </div> -->
              <!-- Skeleton -->
              <!-- <div v-else class="animate-pulse" role="status">
                  <div class="justify-start mt-6">
                    <div
                      class="h-[30px] bg-gray-300 max-w-[135px] mb-2.5 rounded-md mt-1"
                    ></div>
                    <div
                      class="h-[210px] bg-gray-300 max-w-[1230px] mb-2.5 rounded-md"
                    ></div>
                  </div>
                </div>
              </div> -->
              <!-- <div class="sm:col-span-3">
                <div v-if="!isLoading">
                  <label
                    for="country"
                    class="block text-sm font-medium leading-6 text-gray-900"
                    >Categoria</label
                  >
                  <div class="mt-2">
                    <select
                      id="country"
                      name="country"
                      autocomplete="country-name"
                      class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6"
                    >
                      <option>Agronegócio</option>
                      <option>Arquitetura e Construção</option>
                      <option>Autos</option>
                      <option>Beleza e Bem Estar</option>
                      <option>Cidades</option>
                      <option>Comportamento</option>
                      <option>Copa do Mundo</option>
                      <option>Coronavírus</option>
                      <option>Crime</option>
                      <option>Cultura e Lazer</option>
                      <option>Economia</option>
                      <option>Educação</option>
                      <option>Eleições</option>
                      <option>Esportes</option>
                      <option>Gastronomia</option>
                      <option>Meio Ambiente</option>
                      <option>Mercado Imobiliário</option>
                      <option>Mundo</option>
                      <option>Opnião</option>
                      <option>Pets</option>
                      <option>Polícia</option>
                      <option>Política</option>
                      <option>Saúde</option>
                      <option>Serviços</option>
                      <option>Tecnologia e Inovação</option>
                      <option>Trabalho e Emprego</option>
                      <option>Turismo</option>
                      <option>Variedades</option>
                    </select>
                  </div>
                </div> -->
              <!-- Skeleton -->
              <!-- <div v-else class="animate-pulse" role="status">
                  <div class="justify-start mt-6">
                    <div
                      class="h-[30px] bg-gray-300 max-w-[135px] mb-2.5 rounded-md mt-1"
                    ></div>
                    <div
                      class="h-[40px] bg-gray-300 max-w-[320px] mb-2.5 rounded-md"
                    ></div>
                  </div>
                </div>
              </div> -->
            </div>
          </div>

          <!-- <div class="border-b border-gray-900/10 pb-12">
            <div class="mt-10 space-y-10">
              <fieldset v-if="!isLoading">
                <legend class="text-sm font-semibold leading-6 text-gray-900">
                  Posição da Notícia
                </legend>
                <p class="mt-1 text-sm leading-6 text-gray-600">
                  Selecione onde a notícia será posicionada.
                </p>
                <div class="mt-6 space-y-6">
                  <div class="flex items-center gap-x-3">
                    <input
                      id="news-type-normal"
                      name="news-type"
                      type="radio"
                      class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600"
                    />
                    <label
                      for="news-type-normal"
                      class="block text-sm font-medium leading-6 text-gray-900"
                      >Normal</label
                    >
                  </div>
                  <div class="flex items-center gap-x-3">
                    <input
                      id="news-type-carrousel"
                      name="news-type"
                      type="radio"
                      class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600"
                    />
                    <label
                      for="news-type-carrousel"
                      class="block text-sm font-medium leading-6 text-gray-900"
                      >Carrousel</label
                    >
                  </div>
                </div>
              </fieldset> -->
          <!-- Skeleton -->
          <!-- <div v-else class="animate-pulse" role="status">
                <div class="justify-start mt-6">
                  <div
                    class="h-[30px] bg-gray-300 max-w-[135px] mb-2.5 rounded-md mt-1"
                  ></div>
                  <div
                    class="h-[30px] bg-gray-300 max-w-[310px] mb-2.5 rounded-md"
                  ></div>
                  <div class="mt-6">
                    <div
                      class="h-[30px] bg-gray-300 max-w-[310px] mb-2.5 rounded-md"
                    ></div>
                    <div
                      class="h-[30px] bg-gray-300 max-w-[310px] mb-2.5 rounded-md mt-6"
                    ></div>
                  </div>
                </div>
              </div>
            </div>
          </div> -->
        </div>

        <div
          v-if="!isLoading"
          class="mt-6 flex items-center justify-end gap-x-6"
        >
          <button
            type="button"
            @click.prevent="sendSubmission"
            class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Enviar
          </button>
        </div>
        <!-- Skeleton -->
        <div v-else class="animate-pulse" role="status">
          <div class="flex flex-row justify-end mt-6">
            <div
              class="grow items-end h-[40px] bg-gray-300 max-w-[100px] mb-2.5 rounded-md"
            ></div>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>
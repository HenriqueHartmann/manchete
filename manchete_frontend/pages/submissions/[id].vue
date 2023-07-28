<script setup>
import { storeToRefs } from "pinia";
import { useAuthStore } from "../../store/auth";
import { ref } from "vue";

definePageMeta({
  layout: "default",
});
const config = useRuntimeConfig()

const route = useRoute();
const router = useRouter();

const newsId = ref(route.params.id);
const { authenticateUser } = useAuthStore();
const { authenticated } = storeToRefs(useAuthStore());
const token = useCookie("token");

if (!authenticated) {
  router.push("/");
}

const isCommonError = ref(false);
const isPermissionError = ref(false);
const newsBody = ref({
  title: "",
  subtitle: "",
  body: "",
});

const { data, pending, refresh } = await useAsyncData("news", () =>
  $fetch(`${config.public.baseURL}/news/${newsId.value}/`, {
    method: "get",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${token.value}`,
    },
    initialCache: false,
    onResponse({ request, response, options }) {
      newsBody.value.title = response._data["title"];
      newsBody.value.subtitle = response._data["subtitle"];
      newsBody.value.body = response._data["body"];
    },
    onResponseError({ request, response, options }) {
      if (response.status === 403) {
        isPermissionError.value = true;
      } else {
        isCommonError.value = true;
      }
    },
  })
);

const publishNews = async () => {
  const { data, pending } = await useFetch(
    `${config.public.baseURL}/news/publish/${newsId.value}/`,
    {
      method: "put",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token.value}`,
      },
      onResponse({ request, response, options }) {},
      onResponseError({ request, response, options }) {
        console.log("Erro");
        console.log(response.status);
      },
    }
  );
};

const deleteNews = async () => {
  const { data, pending } = await useFetch(
    `${config.public.baseURL}/news/${newsId.value}/`,
    {
      method: "put",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token.value}`,
      },
      onResponse({ request, response, options }) {},
      onResponseError({ request, response, options }) {
        console.log("Erro");
        console.log(response.status);
      },
    }
  );
};

const updateNews = async () => {
  console.log(token.value);
  if (
    newsBody.value.title.length > 0 &&
    newsBody.value.subtitle.length > 0 &&
    newsBody.value.body.length > 0
  ) {
    const { data, pending } = await useFetch(
      `${config.public.baseURL}/news/${newsId.value}/`,
      {
        method: "patch",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${token.value}`,
        },
        body: {
          title: newsBody.value.title,
          subtitle: newsBody.value.subtitle,
          body: newsBody.value.body,
        },
        onResponse({ request, response, options }) {},
        onResponseError({ request, response, options }) {
          console.log("Erro");
          console.log(response.status);
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
  <div class="min-h-full">
    <div
      v-if="pending"
      class="max-w-screen-xl px-4 mx-auto flex justify-center items-center min-h-[730px]"
    >
      <div class="flex justify-center">
        <div class="px-3 py-24">
          <div class="text-slate-800 text-3xl font-semibold">
            Você não possui permissão para acessar este conteúdo.
          </div>
        </div>
      </div>
    </div>
    <div
      v-else-if="isCommonError"
      class="max-w-screen-xl px-4 mx-auto flex justify-center items-center min-h-[730px]"
    >
      <div class="px-3 py-24">
        <div class="text-slate-800 text-3xl font-semibold">
          Um erro inesperado aconteceu.
        </div>
      </div>
    </div>
    <div
      v-else
      v-show="!isPermissionError && !isCommonError"
      class="max-w-screen-xl px-6 pt-4 mx-auto"
    >
      <form>
        <div class="space-y-12">
          <div class="border-b border-gray-900/10 pb-12">
            <div>
              <h2 class="text-base font-semibold leading-7 text-gray-900">
                Notícia
              </h2>
              <p class="mt-1 text-sm leading-6 text-gray-600">
                Crie uma nova notícia para os leitores.
              </p>
            </div>

            <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
              <div class="sm:col-span-4">
                <div>
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
              </div>

              <div class="sm:col-span-4">
                <div>
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
              </div>

              <div class="col-span-full">
                <div>
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
              </div>
            </div>
          </div>
        </div>

        <div class="mt-6 flex items-center justify-end gap-x-6">
          <button
            type="button"
            @click.prevent="sendSubmission"
            class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Enviar
          </button>
        </div>
      </form>
    </div>
  </div>
</template>
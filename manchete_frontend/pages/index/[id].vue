<script setup>
import { storeToRefs } from "pinia";
import { useAuthStore } from "../../store/auth";
import { ref } from "vue";

definePageMeta({
  layout: "default",
});
const config = useRuntimeConfig();

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

const { data, pending, refresh } = await useAsyncData("news", () =>
  $fetch(`${config.public.baseURL}/news/${newsId.value}/`, {
    method: "get",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${token.value}`,
    },
    initialCache: false,
    onResponseError({ request, response, options }) {
      if (response.status === 403) {
        isPermissionError.value = true;
      } else {
        isCommonError.value = true;
      }
    },
  })
);
</script>

<template>
  <div class="min-h-full">
    <div
      v-if="pending"
      class="max-w-screen-xl px-4 mx-auto flex justify-center items-center min-h-[730px]"
    >
      <Loading />
    </div>
    <div
      v-else-if="isPermissionError"
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
    <div v-else class="max-w-screen-xl px-4 pt-4 mx-auto min-h-[700px]">
      <div class="flex flex-row items-center justify-start py-8 px-3">
        <div class="text-slate-800 text-5xl font-semibold">
          {{ data['title'] }}
        </div>
      </div>
      <div class="flex flex-row items-center justify-start py-8 px-3">
        <div class="text-slate-800 text-2xl font-semibold">
          {{ data['subtitle'] }}
        </div>
      </div>
      <div class="flex flex-row items-center justify-start py-8 px-3">
        <div class="text-slate-800 text-md font-semibold">
          Criado por: <b>{{ data["created_by"]["user"]["name"] }}</b>
        </div>
      </div>
      <div class="flex flex-row items-center justify-start py-8 px-3">
        <div class="text-slate-800 text-xl">
          {{ data['body'] }}
        </div>
      </div>
    </div>
  </div>
</template>
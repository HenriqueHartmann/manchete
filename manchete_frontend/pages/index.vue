<script setup>
import { ref } from "vue";

definePageMeta({
  layout: "default",
});
const config = useRuntimeConfig()

const page = ref(1);

const { data, pending, refresh } = await useAsyncData(
  "news",
  () =>
    $fetch(`${config.public.baseURL}/news/?page=${page.value}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
      initialCache: false,
    }),
  {
    watch: [page],
  }
);

const refetch = (value) => {
  page.value = value;
  refresh();
};
</script>

<template>
  <div class="min-h-full">
    <div
      v-if="pending"
      class="max-w-screen-xl px-4 mx-auto flex justify-center items-center min-h-[700px]"
    >
      <Loading />
    </div>
    <div v-else class="max-w-screen-xl px-4 pt-4 mx-auto min-h-[700px]">
      <div class="flex flex-row items-center justify-start py-8 px-3">
        <div class="text-slate-800 text-5xl font-semibold">Notícias</div>
      </div>
      <div v-if="data['count'] === 0" class="flex justify-center">
        <div class="px-3 py-24">
            <div class="text-slate-800 text-3xl font-semibold">
              Sem notícias cadastradas
            </div>
        </div>
      </div>
      <div v-else>
        <div
          class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-3 items-start gap-x-8 gap-y-8 flex-1"
        >
          <div
            v-for="(n, index) in data['results']"
            :key="index"
            class="min-w-full w-full h-full flex justify-center"
          >
            <NewsCard :title="n.title" :subtitle="n.subtitle" />
          </div>
          <div>
        </div>
      </div>
      <div class="pt-[150px] pb-[50px] flex justify-center items-center">
              <ul class="flex justify-center items-center">
                <li v-for="n in data['total_pages']" :key="n">
                  <button
                    v-if="n === page"
                    type="button"
                    class="mx-1 flex h-9 w-9 items-center justify-center rounded-full bg-gradient-to-tr from-purple-600 to-blue-500 p-0 text-sm text-white shadow-md shadow-blue-500/20 transition duration-150 ease-in-out"
                    href="#"
                  >
                    {{ n }}
                  </button>
                  <button
                    type="button"
                    v-else
                    @click="refetch(n)"
                    class="mx-1 flex h-9 w-9 items-center justify-center rounded-full border border-blue-gray-100 bg-transparent p-0 text-sm text-blue-gray-500 transition duration-150 ease-in-out hover:bg-gradient-to-tr from-purple-600 to-blue-500 hover:text-white"
                    href="#"
                  >
                    {{ n }}
                  </button>
                </li>
              </ul>
            </div>
          </div>
    </div>
  </div>
</template>

<style>
.pagination-container {
  display: flex;
  column-gap: 10px;
}
.paginate-buttons {
  height: 40px;
  width: 40px;
  border-radius: 20px;
  cursor: pointer;
  background-color: rgb(255, 255, 255);
  border: 1px solid rgb(217, 217, 217);
  color: black;
}
.paginate-buttons:hover {
  background-color: #d8d8d8;
}
.active-page {
  background-color: rgb(79, 70, 229);
  border: 1px solid rgb(79, 70, 229);
  color: white;
}
.active-page:hover {
  background-color: rgb(67 56 202);
}
</style>
<script setup>
import { ref } from "vue";

definePageMeta({
  layout: "login",
});

const isLoading = ref(true);

setTimeout(() => {
  isLoading.value = false;
}, 1500);
</script>

<template>
  <div>
    <div
      class="min-h-screen bg-gradient-to-br from-sky-50 to-indigo-100 text-gray-900 flex justify-center xl:p-12 lg:p-12"
    >
      <div
        class="max-w-screen-xl m-0 bg-white shadow sm:rounded-lg flex flex-1"
      >
        <LoginForm v-if="!isLoading" />
        <LoginFormSkeleton v-else />
      </div>
    </div>
  </div>
</template>
<template>
  <div
    v-if="!isLoading"
    class="max-w-sm rounded-xl overflow-hidden shadow-lg h-full flex flex-col"
  >
    <!-- IMAGE -->
    <img class="w-full" :src="picture" />

    <!-- CONTENT -->
    <div class="items-end">
      <!-- TITLE -->
      <div class="px-6 py-4">
        <div class="font-bold text-xl mb-2 grow-1">
          {{ title }}
        </div>

        <!-- BODY -->
        <p class="text-gray-700 text-base">
          {{ subtitle }}
        </p>
      </div>

      <!-- CATEGORIES -->
      <!-- <div class="px-6 pt-4 pb-2">
          <span
            v-for="(category, index) in userData.categories"
            :key="index"
            class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
            >{{ category }}</span
          >
        </div> -->
    </div>
  </div>
  <div v-else>
    <NewsCardSkeleton />
  </div>
</template>
  
  <script setup>
import { ref } from "vue";

defineProps({
  title: {type: String, required: true},
  subtitle: {type: String, required: true},
});

const isLoading = ref(true);
const picture =
  "https://unisa.edu.au/siteassets/media-centre/images/coffee_cat_shutterstock_340753520.jpg";

setTimeout(() => {
  isLoading.value = false;
}, 1500);
</script>
  
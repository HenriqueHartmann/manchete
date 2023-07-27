<template>
  <div class="flex justify-center flex-1 animate-pulse">
    <div class="w-full sm:w-5/6 md:w-4/6 lg:w-1/2 xl:w-5/12 p-6 flex flex-col">
      <div class="flex flex-row items-center justify-center py-8 px-3">
        <!-- <LogoTitle /> -->
        <div class="pt-4 pb-2">
          <div class="h-9 w-[255px] bg-gray-200 rounded-full"></div>
        </div>
      </div>
      <div class="flex flex-col items-start justify-center grow pb-20">
        <div class="w-full p-6 space-y-4 md:space-y-6 sm:p-8">
          <div class="pt-4 pb-2">
            <div class="h-9 w-[255px] bg-gray-200 rounded-full"></div>
          </div>
          <div>
            <div class="space-y-4 md:space-y-6">
              <div class="pt-4 pb-2">
                <div class="h-4 w-[80px] bg-gray-200 rounded-full"></div>
              </div>
              <div class="pt-4 pb-2">
                <div class="h-11 bg-gray-200 rounded-full"></div>
              </div>
              <div>
                <div class="pt-4 pb-2">
                  <div class="h-4 w-[80px] bg-gray-200 rounded-full"></div>
                </div>
                <div class="pt-4 pb-2">
                  <div class="h-11 bg-gray-200 rounded-full"></div>
                </div>
              </div>
              <div class="pt-4 pb-2">
                <div class="h-11 bg-gray-200 rounded-full"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="flex-1 bg-gray-100 hidden lg:flex items-center">
      <div class="w-full grid justify-items-center">
        <div
          class="flex items-center justify-center max-w-sm bg-gray-300 rounded-lg w-full h-56"
        >
          <svg
            class="w-10 h-10 text-gray-200"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="currentColor"
            viewBox="0 0 16 20"
          >
            <path
              d="M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.98 2.98 0 0 0 .13 5H5Z"
            />
            <path
              d="M14.066 0H7v5a2 2 0 0 1-2 2H0v11a1.97 1.97 0 0 0 1.934 2h12.132A1.97 1.97 0 0 0 16 18V2a1.97 1.97 0 0 0-1.934-2ZM9 13a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-2a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2Zm4 .382a1 1 0 0 1-1.447.894L10 13v-2l1.553-1.276a1 1 0 0 1 1.447.894v2.764Z"
            />
          </svg>
        </div>
      </div>
    </div>
  </div>
</template>
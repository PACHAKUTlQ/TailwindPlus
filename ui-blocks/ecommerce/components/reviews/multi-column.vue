<template>
  <div class="bg-white">
    <div class="mx-auto max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8">
      <h2 class="text-lg font-medium text-gray-900">Recent reviews</h2>
      <div class="mt-6 divide-y divide-gray-200 border-t border-b border-gray-200">
        <div v-for="review in reviews" :key="review.id" class="py-10 lg:grid lg:grid-cols-12 lg:gap-x-8">
          <div class="lg:col-span-8 lg:col-start-5 xl:col-span-9 xl:col-start-4 xl:grid xl:grid-cols-3 xl:items-start xl:gap-x-8">
            <div class="flex items-center xl:col-span-1">
              <div class="flex items-center">
                <StarIcon v-for="rating in [0, 1, 2, 3, 4]" :key="rating" :class="[review.rating > rating ? 'text-yellow-400' : 'text-gray-200', 'size-5 shrink-0']" aria-hidden="true" />
              </div>
              <p class="ml-3 text-sm text-gray-700">{{ review.rating }}<span class="sr-only"> out of 5 stars</span></p>
            </div>

            <div class="mt-4 lg:mt-6 xl:col-span-2 xl:mt-0">
              <h3 class="text-sm font-medium text-gray-900">{{ review.title }}</h3>

              <div class="mt-3 space-y-6 text-sm text-gray-500" v-html="review.content" />
            </div>
          </div>

          <div class="mt-6 flex items-center text-sm lg:col-span-4 lg:col-start-1 lg:row-start-1 lg:mt-0 lg:flex-col lg:items-start xl:col-span-3">
            <p class="font-medium text-gray-900">{{ review.author }}</p>
            <time :datetime="review.datetime" class="ml-4 border-l border-gray-200 pl-4 text-gray-500 lg:mt-2 lg:ml-0 lg:border-0 lg:pl-0">{{ review.date }}</time>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { StarIcon } from '@heroicons/vue/20/solid'

const reviews = [
  {
    id: 1,
    title: "Can't say enough good things",
    rating: 5,
    content: `
      <p>I was really pleased with the overall shopping experience. My order even included a little personal, handwritten note, which delighted me!</p>
      <p>The product quality is amazing, it looks and feel even better than I had anticipated. Brilliant stuff! I would gladly recommend this store to my friends. And, now that I think of it... I actually have, many times!</p>
    `,
    author: 'Risako M',
    date: 'May 16, 2021',
    datetime: '2021-01-06',
  },
  // More reviews...
]
</script>
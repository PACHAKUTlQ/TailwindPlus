<template>
  <div class="bg-white py-24 sm:py-32">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-2xl text-center">
        <h2 class="text-base/7 font-semibold text-indigo-600">Testimonials</h2>
        <p class="mt-2 text-4xl font-semibold tracking-tight text-balance text-gray-900 sm:text-5xl">We have worked with thousands of amazing people</p>
      </div>
      <div class="mx-auto mt-16 flow-root max-w-2xl sm:mt-20 lg:mx-0 lg:max-w-none">
        <div class="-mt-8 sm:-mx-4 sm:columns-2 sm:text-[0] lg:columns-3">
          <div v-for="testimonial in testimonials" :key="testimonial.author.handle" class="pt-8 sm:inline-block sm:w-full sm:px-4">
            <figure class="rounded-2xl bg-gray-50 p-8 text-sm/6">
              <blockquote class="text-gray-900">
                <p>{{ `“${testimonial.body}”` }}</p>
              </blockquote>
              <figcaption class="mt-6 flex items-center gap-x-4">
                <img class="size-10 rounded-full bg-gray-50" :src="testimonial.author.imageUrl" alt="" />
                <div>
                  <div class="font-semibold text-gray-900">{{ testimonial.author.name }}</div>
                  <div class="text-gray-600">{{ `@${testimonial.author.handle}` }}</div>
                </div>
              </figcaption>
            </figure>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const testimonials = [
  {
    body: 'Laborum quis quam. Dolorum et ut quod quia. Voluptas numquam delectus nihil. Aut enim doloremque et ipsam.',
    author: {
      name: 'Leslie Alexander',
      handle: 'lesliealexander',
      imageUrl:
        'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
    },
  },
  // More testimonials...
]
</script>
<template>
  <div class="bg-white py-24 sm:py-32">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto grid max-w-2xl grid-cols-1 gap-8 overflow-hidden lg:mx-0 lg:max-w-none lg:grid-cols-4">
        <div v-for="item in timeline" :key="item.name">
          <time :datetime="item.dateTime" class="flex items-center text-sm/6 font-semibold text-indigo-600">
            <svg viewBox="0 0 4 4" class="mr-4 size-1 flex-none" aria-hidden="true">
              <circle cx="2" cy="2" r="2" fill="currentColor" />
            </svg>
            {{ item.date }}
            <div class="absolute -ml-2 h-px w-screen -translate-x-full bg-gray-900/10 sm:-ml-4 lg:static lg:-mr-6 lg:ml-8 lg:w-auto lg:flex-auto lg:translate-x-0" aria-hidden="true" />
          </time>
          <p class="mt-6 text-lg/8 font-semibold tracking-tight text-gray-900">{{ item.name }}</p>
          <p class="mt-1 text-base/7 text-gray-600">{{ item.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const timeline = [
  {
    name: 'Founded company',
    description:
      'Nihil aut nam. Dignissimos a pariatur et quos omnis. Aspernatur asperiores et dolorem dolorem optio voluptate repudiandae.',
    date: 'Aug 2021',
    dateTime: '2021-08',
  },
  {
    name: 'Secured $65m in funding',
    description:
      'Provident quia ut esse. Vero vel eos repudiandae aspernatur. Cumque minima impedit sapiente a architecto nihil.',
    date: 'Dec 2021',
    dateTime: '2021-12',
  },
  {
    name: 'Released beta',
    description:
      'Sunt perspiciatis incidunt. Non necessitatibus aliquid. Consequatur ut officiis earum eum quia facilis. Hic deleniti dolorem quia et.',
    date: 'Feb 2022',
    dateTime: '2022-02',
  },
  {
    name: 'Global launch of product',
    description:
      'Ut ipsa sint distinctio quod itaque nam qui. Possimus aut unde id architecto voluptatem hic aut pariatur velit.',
    date: 'Dec 2022',
    dateTime: '2022-12',
  },
]
</script>
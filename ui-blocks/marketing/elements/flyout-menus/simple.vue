<template>
  <Popover class="relative">
    <PopoverButton class="inline-flex items-center gap-x-1 text-sm/6 font-semibold text-gray-900">
      <span>Solutions</span>
      <ChevronDownIcon class="size-5" aria-hidden="true" />
    </PopoverButton>

    <transition enter-active-class="transition ease-out duration-200" enter-from-class="opacity-0 translate-y-1" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition ease-in duration-150" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-1">
      <PopoverPanel class="absolute left-1/2 z-10 mt-5 flex w-screen max-w-min -translate-x-1/2 px-4">
        <div class="w-56 shrink rounded-xl bg-white p-4 text-sm/6 font-semibold text-gray-900 ring-1 shadow-lg ring-gray-900/5">
          <a v-for="item in solutions" :key="item.name" :href="item.href" class="block p-2 hover:text-indigo-600">{{ item.name }}</a>
        </div>
      </PopoverPanel>
    </transition>
  </Popover>
</template>

<script setup>
import { Popover, PopoverButton, PopoverPanel } from '@headlessui/vue'
import { ChevronDownIcon } from '@heroicons/vue/20/solid'

const solutions = [
  { name: 'Analytics', href: '#' },
  { name: 'Engagement', href: '#' },
  { name: 'Security', href: '#' },
  { name: 'Integrations', href: '#' },
  { name: 'Automations', href: '#' },
  { name: 'Reports', href: '#' },
]
</script>
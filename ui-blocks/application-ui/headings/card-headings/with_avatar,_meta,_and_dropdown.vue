<template>
  <div class="bg-white px-4 py-5 sm:px-6">
    <div class="flex space-x-3">
      <div class="shrink-0">
        <img class="size-10 rounded-full" src="https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
      </div>
      <div class="min-w-0 flex-1">
        <p class="text-sm font-semibold text-gray-900">
          <a href="#" class="hover:underline">Chelsea Hagon</a>
        </p>
        <p class="text-sm text-gray-500">
          <a href="#" class="hover:underline">December 9 at 11:43 AM</a>
        </p>
      </div>
      <div class="flex shrink-0 self-center">
        <Menu as="div" class="relative inline-block text-left">
          <div>
            <MenuButton class="-m-2 flex items-center rounded-full p-2 text-gray-400 hover:text-gray-600">
              <span class="sr-only">Open options</span>
              <EllipsisVerticalIcon class="size-5" aria-hidden="true" />
            </MenuButton>
          </div>

          <transition enter-active-class="transition ease-out duration-100" enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100" leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100" leave-to-class="transform opacity-0 scale-95">
            <MenuItems class="absolute right-0 z-10 mt-2 w-56 origin-top-right rounded-md bg-white ring-1 shadow-lg ring-black/5 focus:outline-hidden">
              <div class="py-1">
                <MenuItem v-slot="{ active }">
                  <a href="#" :class="[active ? 'bg-gray-100 text-gray-900 outline-hidden' : 'text-gray-700', 'flex px-4 py-2 text-sm']">
                    <StarIcon class="mr-3 size-5 text-gray-400" aria-hidden="true" />
                    <span>Add to favorites</span>
                  </a>
                </MenuItem>
                <MenuItem v-slot="{ active }">
                  <a href="#" :class="[active ? 'bg-gray-100 text-gray-900 outline-hidden' : 'text-gray-700', 'flex px-4 py-2 text-sm']">
                    <CodeBracketIcon class="mr-3 size-5 text-gray-400" aria-hidden="true" />
                    <span>Embed</span>
                  </a>
                </MenuItem>
                <MenuItem v-slot="{ active }">
                  <a href="#" :class="[active ? 'bg-gray-100 text-gray-900 outline-hidden' : 'text-gray-700', 'flex px-4 py-2 text-sm']">
                    <FlagIcon class="mr-3 size-5 text-gray-400" aria-hidden="true" />
                    <span>Report content</span>
                  </a>
                </MenuItem>
              </div>
            </MenuItems>
          </transition>
        </Menu>
      </div>
    </div>
  </div>
</template>

<script setup>
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
import { CodeBracketIcon, EllipsisVerticalIcon, FlagIcon, StarIcon } from '@heroicons/vue/20/solid'
</script>
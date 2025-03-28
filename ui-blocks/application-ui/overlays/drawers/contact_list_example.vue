<template>
  <TransitionRoot as="template" :show="open">
    <Dialog class="relative z-10" @close="open = false">
      <div class="fixed inset-0" />

      <div class="fixed inset-0 overflow-hidden">
        <div class="absolute inset-0 overflow-hidden">
          <div class="pointer-events-none fixed inset-y-0 right-0 flex max-w-full pl-10 sm:pl-16">
            <TransitionChild as="template" enter="transform transition ease-in-out duration-500 sm:duration-700" enter-from="translate-x-full" enter-to="translate-x-0" leave="transform transition ease-in-out duration-500 sm:duration-700" leave-from="translate-x-0" leave-to="translate-x-full">
              <DialogPanel class="pointer-events-auto w-screen max-w-md">
                <div class="flex h-full flex-col overflow-y-scroll bg-white shadow-xl">
                  <div class="p-6">
                    <div class="flex items-start justify-between">
                      <DialogTitle class="text-base font-semibold text-gray-900">Team</DialogTitle>
                      <div class="ml-3 flex h-7 items-center">
                        <button type="button" class="relative rounded-md bg-white text-gray-400 hover:text-gray-500 focus:ring-2 focus:ring-indigo-500" @click="open = false">
                          <span class="absolute -inset-2.5" />
                          <span class="sr-only">Close panel</span>
                          <XMarkIcon class="size-6" aria-hidden="true" />
                        </button>
                      </div>
                    </div>
                  </div>
                  <div class="border-b border-gray-200">
                    <div class="px-6">
                      <nav class="-mb-px flex space-x-6">
                        <a v-for="tab in tabs" :key="tab.name" :href="tab.href" :class="[tab.current ? 'border-indigo-500 text-indigo-600' : 'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700', 'border-b-2 px-1 pb-4 text-sm font-medium whitespace-nowrap']">{{ tab.name }}</a>
                      </nav>
                    </div>
                  </div>
                  <ul role="list" class="flex-1 divide-y divide-gray-200 overflow-y-auto">
                    <li v-for="person in team" :key="person.handle">
                      <div class="group relative flex items-center px-5 py-6">
                        <a :href="person.href" class="-m-1 block flex-1 p-1">
                          <div class="absolute inset-0 group-hover:bg-gray-50" aria-hidden="true" />
                          <div class="relative flex min-w-0 flex-1 items-center">
                            <span class="relative inline-block shrink-0">
                              <img class="size-10 rounded-full" :src="person.imageUrl" alt="" />
                              <span :class="[person.status === 'online' ? 'bg-green-400' : 'bg-gray-300', 'absolute top-0 right-0 block size-2.5 rounded-full ring-2 ring-white']" aria-hidden="true" />
                            </span>
                            <div class="ml-4 truncate">
                              <p class="truncate text-sm font-medium text-gray-900">{{ person.name }}</p>
                              <p class="truncate text-sm text-gray-500">{{ '@' + person.handle }}</p>
                            </div>
                          </div>
                        </a>
                        <Menu as="div" class="relative ml-2 inline-block shrink-0 text-left">
                          <MenuButton class="group relative inline-flex size-8 items-center justify-center rounded-full bg-white focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:outline-hidden">
                            <span class="absolute -inset-1.5" />
                            <span class="sr-only">Open options menu</span>
                            <span class="flex size-full items-center justify-center rounded-full">
                              <EllipsisVerticalIcon class="size-5 text-gray-400 group-hover:text-gray-500" aria-hidden="true" />
                            </span>
                          </MenuButton>
                          <transition enter-active-class="transition ease-out duration-100" enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100" leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100" leave-to-class="transform opacity-0 scale-95">
                            <MenuItems class="absolute top-0 right-9 z-10 w-48 origin-top-right rounded-md bg-white ring-1 shadow-lg ring-black/5 focus:outline-hidden">
                              <div class="py-1">
                                <MenuItem v-slot="{ active }">
                                  <a href="#" :class="[active ? 'bg-gray-100 text-gray-900 outline-hidden' : 'text-gray-700', 'block px-4 py-2 text-sm']">View profile</a>
                                </MenuItem>
                                <MenuItem v-slot="{ active }">
                                  <a href="#" :class="[active ? 'bg-gray-100 text-gray-900 outline-hidden' : 'text-gray-700', 'block px-4 py-2 text-sm']">Send message</a>
                                </MenuItem>
                              </div>
                            </MenuItems>
                          </transition>
                        </Menu>
                      </div>
                    </li>
                  </ul>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>

<script setup>
import { ref } from 'vue'
import {
  Dialog,
  DialogPanel,
  DialogTitle,
  Menu,
  MenuButton,
  MenuItem,
  MenuItems,
  TransitionChild,
  TransitionRoot,
} from '@headlessui/vue'
import { XMarkIcon } from '@heroicons/vue/24/outline'
import { EllipsisVerticalIcon } from '@heroicons/vue/20/solid'

const tabs = [
  { name: 'All', href: '#', current: true },
  { name: 'Online', href: '#', current: false },
  { name: 'Offline', href: '#', current: false },
]
const team = [
  {
    name: 'Leslie Alexander',
    handle: 'lesliealexander',
    href: '#',
    imageUrl:
      'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
    status: 'online',
  },
  // More people...
]

const open = ref(true)
</script>
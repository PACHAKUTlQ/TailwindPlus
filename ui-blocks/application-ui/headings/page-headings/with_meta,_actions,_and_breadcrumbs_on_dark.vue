<template>
  <div class="lg:flex lg:items-center lg:justify-between">
    <div class="min-w-0 flex-1">
      <nav class="flex" aria-label="Breadcrumb">
        <ol role="list" class="flex items-center space-x-4">
          <li>
            <div class="flex">
              <a href="#" class="text-sm font-medium text-gray-300 hover:text-white">Jobs</a>
            </div>
          </li>
          <li>
            <div class="flex items-center">
              <ChevronRightIcon class="size-5 shrink-0 text-gray-500" aria-hidden="true" />
              <a href="#" class="ml-4 text-sm font-medium text-gray-300 hover:text-white">Engineering</a>
            </div>
          </li>
        </ol>
      </nav>
      <h2 class="mt-2 text-2xl/7 font-bold text-white sm:truncate sm:text-3xl sm:tracking-tight">Back End Developer</h2>
      <div class="mt-1 flex flex-col sm:mt-0 sm:flex-row sm:flex-wrap sm:space-x-6">
        <div class="mt-2 flex items-center text-sm text-gray-300">
          <BriefcaseIcon class="mr-1.5 size-5 shrink-0 text-gray-500" aria-hidden="true" />
          Full-time
        </div>
        <div class="mt-2 flex items-center text-sm text-gray-300">
          <MapPinIcon class="mr-1.5 size-5 shrink-0 text-gray-500" aria-hidden="true" />
          Remote
        </div>
        <div class="mt-2 flex items-center text-sm text-gray-300">
          <CurrencyDollarIcon class="mr-1.5 size-5 shrink-0 text-gray-500" aria-hidden="true" />
          $120k – $140k
        </div>
        <div class="mt-2 flex items-center text-sm text-gray-300">
          <CalendarIcon class="mr-1.5 size-5 shrink-0 text-gray-500" aria-hidden="true" />
          Closing on January 9, 2020
        </div>
      </div>
    </div>
    <div class="mt-5 flex lg:mt-0 lg:ml-4">
      <span class="hidden sm:block">
        <button type="button" class="inline-flex items-center rounded-md bg-white/10 px-3 py-2 text-sm font-semibold text-white shadow-xs hover:bg-white/20">
          <PencilIcon class="mr-1.5 -ml-0.5 size-5" aria-hidden="true" />
          Edit
        </button>
      </span>
      <span class="ml-3 hidden sm:block">
        <button type="button" class="inline-flex items-center rounded-md bg-white/10 px-3 py-2 text-sm font-semibold text-white shadow-xs hover:bg-white/20">
          <LinkIcon class="mr-1.5 -ml-0.5 size-5" aria-hidden="true" />
          View
        </button>
      </span>
      <span class="sm:ml-3">
        <button type="button" class="inline-flex items-center rounded-md bg-indigo-500 px-3 py-2 text-sm font-semibold text-white shadow-xs hover:bg-indigo-400 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500">
          <CheckIcon class="mr-1.5 -ml-0.5 size-5" aria-hidden="true" />
          Publish
        </button>
      </span>

      <!-- Dropdown -->
      <Menu as="div" class="relative ml-3 sm:hidden">
        <MenuButton class="inline-flex items-center rounded-md bg-white/10 px-3 py-2 text-sm font-semibold text-white shadow-xs hover:bg-white/20">
          More
          <ChevronDownIcon class="-mr-1 ml-1.5 size-5" aria-hidden="true" />
        </MenuButton>
        <transition enter-active-class="transition ease-out duration-200" enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100" leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100" leave-to-class="transform opacity-0 scale-95">
          <MenuItems class="absolute left-0 z-10 mt-2 -ml-1 w-48 origin-top-left rounded-md bg-white py-1 ring-1 shadow-lg ring-black/5 focus:outline-hidden">
            <MenuItem v-slot="{ active }">
              <a href="#" :class="[active ? 'bg-gray-100 outline-hidden' : '', 'block px-4 py-2 text-sm text-gray-700']">Edit</a>
            </MenuItem>
            <MenuItem v-slot="{ active }">
              <a href="#" :class="[active ? 'bg-gray-100 outline-hidden' : '', 'block px-4 py-2 text-sm text-gray-700']">View</a>
            </MenuItem>
          </MenuItems>
        </transition>
      </Menu>
    </div>
  </div>
</template>

<script setup>
import {
  BriefcaseIcon,
  CalendarIcon,
  CheckIcon,
  ChevronDownIcon,
  ChevronRightIcon,
  CurrencyDollarIcon,
  LinkIcon,
  MapPinIcon,
  PencilIcon,
} from '@heroicons/vue/20/solid'
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
</script>
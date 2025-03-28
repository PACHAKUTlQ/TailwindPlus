<template>
  <TransitionRoot :show="open" as="template" @after-leave="query = ''" appear>
    <Dialog class="relative z-10" @close="open = false">
      <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100" leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
        <div class="fixed inset-0 bg-gray-500/25 transition-opacity" />
      </TransitionChild>

      <div class="fixed inset-0 z-10 w-screen overflow-y-auto p-4 sm:p-6 md:p-20">
        <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0 scale-95" enter-to="opacity-100 scale-100" leave="ease-in duration-200" leave-from="opacity-100 scale-100" leave-to="opacity-0 scale-95">
          <DialogPanel class="mx-auto max-w-3xl transform divide-y divide-gray-100 overflow-hidden rounded-xl bg-white ring-1 shadow-2xl ring-black/5 transition-all">
            <Combobox v-slot="{ activeOption }" @update:modelValue="onSelect">
              <div class="grid grid-cols-1">
                <ComboboxInput class="col-start-1 row-start-1 h-12 w-full pr-4 pl-11 text-base text-gray-900 outline-hidden placeholder:text-gray-400 sm:text-sm" placeholder="Search..." @change="query = $event.target.value" @blur="query = ''" />
                <MagnifyingGlassIcon class="pointer-events-none col-start-1 row-start-1 ml-4 size-5 self-center text-gray-400" aria-hidden="true" />
              </div>

              <ComboboxOptions v-if="query === '' || filteredPeople.length > 0" class="flex transform-gpu divide-x divide-gray-100" as="div" static hold>
                <div :class="['max-h-96 min-w-0 flex-auto scroll-py-4 overflow-y-auto px-6 py-4', activeOption && 'sm:h-96']">
                  <h2 v-if="query === ''" class="mt-2 mb-4 text-xs font-semibold text-gray-500">Recent searches</h2>
                  <div hold class="-mx-2 text-sm text-gray-700">
                    <ComboboxOption v-for="person in query === '' ? recent : filteredPeople" :key="person.id" :value="person" as="template" v-slot="{ active }">
                      <div :class="['group flex cursor-default items-center rounded-md p-2 select-none', active && 'bg-gray-100 text-gray-900 outline-hidden']">
                        <img :src="person.imageUrl" alt="" class="size-6 flex-none rounded-full" />
                        <span class="ml-3 flex-auto truncate">{{ person.name }}</span>
                        <ChevronRightIcon v-if="active" class="ml-3 size-5 flex-none text-gray-400" aria-hidden="true" />
                      </div>
                    </ComboboxOption>
                  </div>
                </div>

                <div v-if="activeOption" class="hidden h-96 w-1/2 flex-none flex-col divide-y divide-gray-100 overflow-y-auto sm:flex">
                  <div class="flex-none p-6 text-center">
                    <img :src="activeOption.imageUrl" alt="" class="mx-auto size-16 rounded-full" />
                    <h2 class="mt-3 font-semibold text-gray-900">
                      {{ activeOption.name }}
                    </h2>
                    <p class="text-sm/6 text-gray-500">{{ activeOption.role }}</p>
                  </div>
                  <div class="flex flex-auto flex-col justify-between p-6">
                    <dl class="grid grid-cols-1 gap-x-6 gap-y-3 text-sm text-gray-700">
                      <dt class="col-end-1 font-semibold text-gray-900">Phone</dt>
                      <dd>{{ activeOption.phone }}</dd>
                      <dt class="col-end-1 font-semibold text-gray-900">URL</dt>
                      <dd class="truncate">
                        <a :href="activeOption.url" class="text-indigo-600 underline">
                          {{ activeOption.url }}
                        </a>
                      </dd>
                      <dt class="col-end-1 font-semibold text-gray-900">Email</dt>
                      <dd class="truncate">
                        <a :href="`mailto:${activeOption.email}`" class="text-indigo-600 underline">
                          {{ activeOption.email }}
                        </a>
                      </dd>
                    </dl>
                    <button type="button" class="mt-6 w-full rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Send message</button>
                  </div>
                </div>
              </ComboboxOptions>

              <div v-if="query !== '' && filteredPeople.length === 0" class="px-6 py-14 text-center text-sm sm:px-14">
                <UsersIcon class="mx-auto size-6 text-gray-400" aria-hidden="true" />
                <p class="mt-4 font-semibold text-gray-900">No people found</p>
                <p class="mt-2 text-gray-500">We couldn’t find anything with that term. Please try again.</p>
              </div>
            </Combobox>
          </DialogPanel>
        </TransitionChild>
      </div>
    </Dialog>
  </TransitionRoot>
</template>

<script setup>
import { computed, ref } from 'vue'
import { MagnifyingGlassIcon } from '@heroicons/vue/20/solid'
import { ChevronRightIcon, UsersIcon } from '@heroicons/vue/24/outline'
import {
  Combobox,
  ComboboxInput,
  ComboboxOptions,
  ComboboxOption,
  Dialog,
  DialogPanel,
  TransitionChild,
  TransitionRoot,
} from '@headlessui/vue'

const people = [
  {
    id: 1,
    name: 'Leslie Alexander',
    phone: '1-493-747-9031',
    email: 'lesliealexander@example.com',
    role: 'Co-Founder / CEO',
    url: 'https://example.com',
    profileUrl: '#',
    imageUrl:
      'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
  },
  // More people...
]

const recent = [people[5], people[4], people[2], people[10], people[16]]

const open = ref(true)
const query = ref('')
const filteredPeople = computed(() =>
  query.value === ''
    ? []
    : people.filter((person) => {
        return person.name.toLowerCase().includes(query.value.toLowerCase())
      }),
)

function onSelect(person) {
  if (person) {
    window.location = person.url
  }
}
</script>
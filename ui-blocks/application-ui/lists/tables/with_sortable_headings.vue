<template>
  <div class="px-4 sm:px-6 lg:px-8">
    <div class="sm:flex sm:items-center">
      <div class="sm:flex-auto">
        <h1 class="text-base font-semibold text-gray-900">Users</h1>
        <p class="mt-2 text-sm text-gray-700">A list of all the users in your account including their name, title, email and role.</p>
      </div>
      <div class="mt-4 sm:mt-0 sm:ml-16 sm:flex-none">
        <button type="button" class="block rounded-md bg-indigo-600 px-3 py-2 text-center text-sm font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Add user</button>
      </div>
    </div>
    <div class="mt-8 flow-root">
      <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
          <table class="min-w-full divide-y divide-gray-300">
            <thead>
              <tr>
                <th scope="col" class="py-3.5 pr-3 pl-4 text-left text-sm font-semibold text-gray-900 sm:pl-0">
                  <a href="#" class="group inline-flex">
                    Name
                    <span class="invisible ml-2 flex-none rounded-sm text-gray-400 group-hover:visible group-focus:visible">
                      <ChevronDownIcon class="size-5" aria-hidden="true" />
                    </span>
                  </a>
                </th>
                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">
                  <a href="#" class="group inline-flex">
                    Title
                    <span class="ml-2 flex-none rounded-sm bg-gray-100 text-gray-900 group-hover:bg-gray-200">
                      <ChevronDownIcon class="size-5" aria-hidden="true" />
                    </span>
                  </a>
                </th>
                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">
                  <a href="#" class="group inline-flex">
                    Email
                    <span class="invisible ml-2 flex-none rounded-sm text-gray-400 group-hover:visible group-focus:visible">
                      <ChevronDownIcon class="invisible ml-2 size-5 flex-none rounded-sm text-gray-400 group-hover:visible group-focus:visible" aria-hidden="true" />
                    </span>
                  </a>
                </th>
                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">
                  <a href="#" class="group inline-flex">
                    Role
                    <span class="invisible ml-2 flex-none rounded-sm text-gray-400 group-hover:visible group-focus:visible">
                      <ChevronDownIcon class="invisible ml-2 size-5 flex-none rounded-sm text-gray-400 group-hover:visible group-focus:visible" aria-hidden="true" />
                    </span>
                  </a>
                </th>
                <th scope="col" class="relative py-3.5 pr-0 pl-3">
                  <span class="sr-only">Edit</span>
                </th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200 bg-white">
              <tr v-for="person in people" :key="person.email">
                <td class="py-4 pr-3 pl-4 text-sm font-medium whitespace-nowrap text-gray-900 sm:pl-0">{{ person.name }}</td>
                <td class="px-3 py-4 text-sm whitespace-nowrap text-gray-500">{{ person.title }}</td>
                <td class="px-3 py-4 text-sm whitespace-nowrap text-gray-500">{{ person.email }}</td>
                <td class="px-3 py-4 text-sm whitespace-nowrap text-gray-500">{{ person.role }}</td>
                <td class="relative py-4 pr-4 pl-3 text-right text-sm whitespace-nowrap sm:pr-0">
                  <a href="#" class="text-indigo-600 hover:text-indigo-900"
                    >Edit<span class="sr-only">, {{ person.name }}</span></a
                  >
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ChevronDownIcon } from '@heroicons/vue/20/solid'

const people = [
  { name: 'Lindsay Walton', title: 'Front-end Developer', email: 'lindsay.walton@example.com', role: 'Member' },
  // More people...
]
</script>
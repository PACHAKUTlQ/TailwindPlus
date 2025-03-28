<template>
  <header class="absolute inset-x-0 top-0 z-50 flex h-16 border-b border-gray-900/10">
    <div class="mx-auto flex w-full max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
      <div class="flex flex-1 items-center gap-x-6">
        <button type="button" class="-m-3 p-3 md:hidden" @click="mobileMenuOpen = true">
          <span class="sr-only">Open main menu</span>
          <Bars3Icon class="size-5 text-gray-900" aria-hidden="true" />
        </button>
        <img class="h-8 w-auto" src="/plus-assets/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company" />
      </div>
      <nav class="hidden md:flex md:gap-x-11 md:text-sm/6 md:font-semibold md:text-gray-700">
        <a v-for="(item, itemIdx) in navigation" :key="itemIdx" :href="item.href">{{ item.name }}</a>
      </nav>
      <div class="flex flex-1 items-center justify-end gap-x-8">
        <button type="button" class="-m-2.5 p-2.5 text-gray-400 hover:text-gray-500">
          <span class="sr-only">View notifications</span>
          <BellIcon class="size-6" aria-hidden="true" />
        </button>
        <a href="#" class="-m-1.5 p-1.5">
          <span class="sr-only">Your profile</span>
          <img class="size-8 rounded-full bg-gray-800" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
        </a>
      </div>
    </div>
    <Dialog class="lg:hidden" @close="mobileMenuOpen = false" :open="mobileMenuOpen">
      <div class="fixed inset-0 z-50" />
      <DialogPanel class="fixed inset-y-0 left-0 z-50 w-full overflow-y-auto bg-white px-4 pb-6 sm:max-w-sm sm:px-6 sm:ring-1 sm:ring-gray-900/10">
        <div class="-ml-0.5 flex h-16 items-center gap-x-6">
          <button type="button" class="-m-2.5 p-2.5 text-gray-700" @click="mobileMenuOpen = false">
            <span class="sr-only">Close menu</span>
            <XMarkIcon class="size-6" aria-hidden="true" />
          </button>
          <div class="-ml-0.5">
            <a href="#" class="-m-1.5 block p-1.5">
              <span class="sr-only">Your Company</span>
              <img class="h-8 w-auto" src="/plus-assets/img/logos/mark.svg?color=indigo&shade=600" alt="" />
            </a>
          </div>
        </div>
        <div class="mt-2 space-y-2">
          <a v-for="item in navigation" :key="item.name" :href="item.href" class="-mx-3 block rounded-lg px-3 py-2 text-base/7 font-semibold text-gray-900 hover:bg-gray-50">{{ item.name }}</a>
        </div>
      </DialogPanel>
    </Dialog>
  </header>

  <div class="mx-auto max-w-7xl pt-16 lg:flex lg:gap-x-16 lg:px-8">
    <h1 class="sr-only">General Settings</h1>

    <aside class="flex overflow-x-auto border-b border-gray-900/5 py-4 lg:block lg:w-64 lg:flex-none lg:border-0 lg:py-20">
      <nav class="flex-none px-4 sm:px-6 lg:px-0">
        <ul role="list" class="flex gap-x-3 gap-y-1 whitespace-nowrap lg:flex-col">
          <li v-for="item in secondaryNavigation" :key="item.name">
            <a :href="item.href" :class="[item.current ? 'bg-gray-50 text-indigo-600' : 'text-gray-700 hover:bg-gray-50 hover:text-indigo-600', 'group flex gap-x-3 rounded-md py-2 pr-3 pl-2 text-sm/6 font-semibold']">
              <component :is="item.icon" :class="[item.current ? 'text-indigo-600' : 'text-gray-400 group-hover:text-indigo-600', 'size-6 shrink-0']" aria-hidden="true" />
              {{ item.name }}
            </a>
          </li>
        </ul>
      </nav>
    </aside>

    <main class="px-4 py-16 sm:px-6 lg:flex-auto lg:px-0 lg:py-20">
      <div class="mx-auto max-w-2xl space-y-16 sm:space-y-20 lg:mx-0 lg:max-w-none">
        <div>
          <h2 class="text-base/7 font-semibold text-gray-900">Profile</h2>
          <p class="mt-1 text-sm/6 text-gray-500">This information will be displayed publicly so be careful what you share.</p>

          <dl class="mt-6 divide-y divide-gray-100 border-t border-gray-200 text-sm/6">
            <div class="py-6 sm:flex">
              <dt class="font-medium text-gray-900 sm:w-64 sm:flex-none sm:pr-6">Full name</dt>
              <dd class="mt-1 flex justify-between gap-x-6 sm:mt-0 sm:flex-auto">
                <div class="text-gray-900">Tom Cook</div>
                <button type="button" class="font-semibold text-indigo-600 hover:text-indigo-500">Update</button>
              </dd>
            </div>
            <div class="py-6 sm:flex">
              <dt class="font-medium text-gray-900 sm:w-64 sm:flex-none sm:pr-6">Email address</dt>
              <dd class="mt-1 flex justify-between gap-x-6 sm:mt-0 sm:flex-auto">
                <div class="text-gray-900">tom.cook@example.com</div>
                <button type="button" class="font-semibold text-indigo-600 hover:text-indigo-500">Update</button>
              </dd>
            </div>
            <div class="py-6 sm:flex">
              <dt class="font-medium text-gray-900 sm:w-64 sm:flex-none sm:pr-6">Title</dt>
              <dd class="mt-1 flex justify-between gap-x-6 sm:mt-0 sm:flex-auto">
                <div class="text-gray-900">Human Resources Manager</div>
                <button type="button" class="font-semibold text-indigo-600 hover:text-indigo-500">Update</button>
              </dd>
            </div>
          </dl>
        </div>

        <div>
          <h2 class="text-base/7 font-semibold text-gray-900">Bank accounts</h2>
          <p class="mt-1 text-sm/6 text-gray-500">Connect bank accounts to your account.</p>

          <ul role="list" class="mt-6 divide-y divide-gray-100 border-t border-gray-200 text-sm/6">
            <li class="flex justify-between gap-x-6 py-6">
              <div class="font-medium text-gray-900">TD Canada Trust</div>
              <button type="button" class="font-semibold text-indigo-600 hover:text-indigo-500">Update</button>
            </li>
            <li class="flex justify-between gap-x-6 py-6">
              <div class="font-medium text-gray-900">Royal Bank of Canada</div>
              <button type="button" class="font-semibold text-indigo-600 hover:text-indigo-500">Update</button>
            </li>
          </ul>

          <div class="flex border-t border-gray-100 pt-6">
            <button type="button" class="text-sm/6 font-semibold text-indigo-600 hover:text-indigo-500"><span aria-hidden="true">+</span> Add another bank</button>
          </div>
        </div>

        <div>
          <h2 class="text-base/7 font-semibold text-gray-900">Integrations</h2>
          <p class="mt-1 text-sm/6 text-gray-500">Connect applications to your account.</p>

          <ul role="list" class="mt-6 divide-y divide-gray-100 border-t border-gray-200 text-sm/6">
            <li class="flex justify-between gap-x-6 py-6">
              <div class="font-medium text-gray-900">QuickBooks</div>
              <button type="button" class="font-semibold text-indigo-600 hover:text-indigo-500">Update</button>
            </li>
          </ul>

          <div class="flex border-t border-gray-100 pt-6">
            <button type="button" class="text-sm/6 font-semibold text-indigo-600 hover:text-indigo-500"><span aria-hidden="true">+</span> Add another application</button>
          </div>
        </div>

        <div>
          <h2 class="text-base/7 font-semibold text-gray-900">Language and dates</h2>
          <p class="mt-1 text-sm/6 text-gray-500">Choose what language and date format to use throughout your account.</p>

          <dl class="mt-6 divide-y divide-gray-100 border-t border-gray-200 text-sm/6">
            <div class="py-6 sm:flex">
              <dt class="font-medium text-gray-900 sm:w-64 sm:flex-none sm:pr-6">Language</dt>
              <dd class="mt-1 flex justify-between gap-x-6 sm:mt-0 sm:flex-auto">
                <div class="text-gray-900">English</div>
                <button type="button" class="font-semibold text-indigo-600 hover:text-indigo-500">Update</button>
              </dd>
            </div>
            <div class="py-6 sm:flex">
              <dt class="font-medium text-gray-900 sm:w-64 sm:flex-none sm:pr-6">Date format</dt>
              <dd class="mt-1 flex justify-between gap-x-6 sm:mt-0 sm:flex-auto">
                <div class="text-gray-900">DD-MM-YYYY</div>
                <button type="button" class="font-semibold text-indigo-600 hover:text-indigo-500">Update</button>
              </dd>
            </div>
            <SwitchGroup as="div" class="flex pt-6">
              <SwitchLabel as="dt" class="flex-none pr-6 font-medium text-gray-900 sm:w-64" passive>Automatic timezone</SwitchLabel>
              <dd class="flex flex-auto items-center justify-end">
                <Switch v-model="automaticTimezoneEnabled" :class="[automaticTimezoneEnabled ? 'bg-indigo-600' : 'bg-gray-200', 'flex w-8 cursor-pointer rounded-full p-px ring-1 ring-gray-900/5 transition-colors duration-200 ease-in-out ring-inset focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600']">
                  <span aria-hidden="true" :class="[automaticTimezoneEnabled ? 'translate-x-3.5' : 'translate-x-0', 'size-4 transform rounded-full bg-white ring-1 shadow-xs ring-gray-900/5 transition duration-200 ease-in-out']" />
                </Switch>
              </dd>
            </SwitchGroup>
          </dl>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { Dialog, DialogPanel, Switch, SwitchGroup, SwitchLabel } from '@headlessui/vue'
import { Bars3Icon } from '@heroicons/vue/20/solid'
import {
  BellIcon,
  CreditCardIcon,
  CubeIcon,
  FingerPrintIcon,
  UserCircleIcon,
  UsersIcon,
  XMarkIcon,
} from '@heroicons/vue/24/outline'

const navigation = [
  { name: 'Home', href: '#' },
  { name: 'Invoices', href: '#' },
  { name: 'Clients', href: '#' },
  { name: 'Expenses', href: '#' },
]
const secondaryNavigation = [
  { name: 'General', href: '#', icon: UserCircleIcon, current: true },
  { name: 'Security', href: '#', icon: FingerPrintIcon, current: false },
  { name: 'Notifications', href: '#', icon: BellIcon, current: false },
  { name: 'Plan', href: '#', icon: CubeIcon, current: false },
  { name: 'Billing', href: '#', icon: CreditCardIcon, current: false },
  { name: 'Team members', href: '#', icon: UsersIcon, current: false },
]

const mobileMenuOpen = ref(false)
const automaticTimezoneEnabled = ref(true)
</script>
<template>
  <div class="lg:col-start-3 lg:row-end-1">
    <h2 class="sr-only">Summary</h2>
    <div class="rounded-lg bg-gray-50 ring-1 shadow-xs ring-gray-900/5">
      <dl class="flex flex-wrap">
        <div class="flex-auto pt-6 pl-6">
          <dt class="text-sm/6 font-semibold text-gray-900">Amount</dt>
          <dd class="mt-1 text-base font-semibold text-gray-900">$10,560.00</dd>
        </div>
        <div class="flex-none self-end px-6 pt-4">
          <dt class="sr-only">Status</dt>
          <dd class="inline-flex items-center rounded-md bg-green-50 px-2 py-1 text-xs font-medium text-green-700 ring-1 ring-green-600/20 ring-inset">Paid</dd>
        </div>
        <div class="mt-6 flex w-full flex-none gap-x-4 border-t border-gray-900/5 px-6 pt-6">
          <dt class="flex-none">
            <span class="sr-only">Client</span>
            <UserCircleIcon class="h-6 w-5 text-gray-400" aria-hidden="true" />
          </dt>
          <dd class="text-sm/6 font-medium text-gray-900">Alex Curren</dd>
        </div>
        <div class="mt-4 flex w-full flex-none gap-x-4 px-6">
          <dt class="flex-none">
            <span class="sr-only">Due date</span>
            <CalendarDaysIcon class="h-6 w-5 text-gray-400" aria-hidden="true" />
          </dt>
          <dd class="text-sm/6 text-gray-500">
            <time datetime="2023-01-31">January 31, 2023</time>
          </dd>
        </div>
        <div class="mt-4 flex w-full flex-none gap-x-4 px-6">
          <dt class="flex-none">
            <span class="sr-only">Status</span>
            <CreditCardIcon class="h-6 w-5 text-gray-400" aria-hidden="true" />
          </dt>
          <dd class="text-sm/6 text-gray-500">Paid with MasterCard</dd>
        </div>
      </dl>
      <div class="mt-6 border-t border-gray-900/5 px-6 py-6">
        <a href="#" class="text-sm/6 font-semibold text-gray-900">Download receipt <span aria-hidden="true">&rarr;</span></a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { CalendarDaysIcon, CreditCardIcon, UserCircleIcon } from '@heroicons/vue/20/solid'
</script>
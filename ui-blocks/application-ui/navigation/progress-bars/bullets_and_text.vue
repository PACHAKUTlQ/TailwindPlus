<template>
  <div class="px-4 py-12 sm:px-6 lg:px-8">
    <nav class="flex justify-center" aria-label="Progress">
      <ol role="list" class="space-y-6">
        <li v-for="step in steps" :key="step.name">
          <a v-if="step.status === 'complete'" :href="step.href" class="group">
            <span class="flex items-start">
              <span class="relative flex size-5 shrink-0 items-center justify-center">
                <CheckCircleIcon class="size-full text-indigo-600 group-hover:text-indigo-800" aria-hidden="true" />
              </span>
              <span class="ml-3 text-sm font-medium text-gray-500 group-hover:text-gray-900">{{ step.name }}</span>
            </span>
          </a>
          <a v-else-if="step.status === 'current'" :href="step.href" class="flex items-start" aria-current="step">
            <span class="relative flex size-5 shrink-0 items-center justify-center" aria-hidden="true">
              <span class="absolute size-4 rounded-full bg-indigo-200" />
              <span class="relative block size-2 rounded-full bg-indigo-600" />
            </span>
            <span class="ml-3 text-sm font-medium text-indigo-600">{{ step.name }}</span>
          </a>
          <a v-else :href="step.href" class="group">
            <div class="flex items-start">
              <div class="relative flex size-5 shrink-0 items-center justify-center" aria-hidden="true">
                <div class="size-2 rounded-full bg-gray-300 group-hover:bg-gray-400" />
              </div>
              <p class="ml-3 text-sm font-medium text-gray-500 group-hover:text-gray-900">{{ step.name }}</p>
            </div>
          </a>
        </li>
      </ol>
    </nav>
  </div>
</template>

<script setup>
import { CheckCircleIcon } from '@heroicons/vue/20/solid'

const steps = [
  { name: 'Create account', href: '#', status: 'complete' },
  { name: 'Profile information', href: '#', status: 'current' },
  { name: 'Theme', href: '#', status: 'upcoming' },
  { name: 'Preview', href: '#', status: 'upcoming' },
]
</script>
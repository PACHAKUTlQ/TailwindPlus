<template>
  <div class="bg-white">
    <section aria-labelledby="features-heading" class="relative">
      <img src="/plus-assets/img/ecommerce-images/confirmation-page-01-hero.jpg" alt="Black leather journal with silver steel disc binding resting on wooden shelf with machined steel pen." class="aspect-3/2 w-full object-cover sm:aspect-5/2 lg:absolute lg:aspect-auto lg:h-full lg:w-1/2 lg:pr-4 xl:pr-16" />

      <div class="mx-auto max-w-2xl px-4 pt-16 pb-24 sm:px-6 sm:pb-32 lg:grid lg:max-w-7xl lg:grid-cols-2 lg:gap-x-8 lg:px-8 lg:pt-32">
        <div class="lg:col-start-2">
          <h2 id="features-heading" class="font-medium text-gray-500">Leatherbound Daily Journal</h2>
          <p class="mt-4 text-4xl font-bold tracking-tight text-gray-900">All in the Details</p>
          <p class="mt-4 text-gray-500">We've obsessed over every detail of this handcrafted journal to bring you the best materials for daily use.</p>

          <dl class="mt-10 grid grid-cols-1 gap-x-8 gap-y-10 text-sm sm:grid-cols-2">
            <div v-for="feature in features" :key="feature.name">
              <dt class="font-medium text-gray-900">{{ feature.name }}</dt>
              <dd class="mt-2 text-gray-500">{{ feature.description }}</dd>
            </div>
          </dl>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
const features = [
  {
    name: 'Durable',
    description: 'The leather cover and machined steel disc binding stand up to daily use for years to come.',
  },
  {
    name: 'Refillable',
    description: 'Buy it once and refill as often as you need. Subscribe and save on routine refills.',
  },
  {
    name: 'Thoughtfully designed',
    description:
      'The comfortable disc binding allows you to quickly rearrange pages or combine lined, graph, and blank refills.',
  },
  { name: 'Locally made', description: 'Responsibly and sustainably made real close to wherever you are, somehow.' },
]
</script>
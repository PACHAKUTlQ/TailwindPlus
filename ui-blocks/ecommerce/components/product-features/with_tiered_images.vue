<template>
  <div class="bg-white">
    <div class="mx-auto max-w-2xl px-4 py-24 sm:px-6 sm:py-32 lg:max-w-7xl lg:px-8">
      <div class="grid grid-cols-1 items-center gap-x-8 gap-y-16 lg:grid-cols-2">
        <div>
          <div class="border-b border-gray-200 pb-10">
            <h2 class="font-medium text-gray-500">Machined Kettle</h2>
            <p class="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Elegant simplicity</p>
          </div>

          <dl class="mt-10 space-y-10">
            <div v-for="feature in features" :key="feature.name">
              <dt class="text-sm font-medium text-gray-900">{{ feature.name }}</dt>
              <dd class="mt-3 text-sm text-gray-500">{{ feature.description }}</dd>
            </div>
          </dl>
        </div>

        <div>
          <img src="/plus-assets/img/ecommerce-images/product-feature-09-main-detail.jpg" alt="Black kettle with long pour spot and angled body on marble counter next to coffee mug and pour-over system." class="aspect-square w-full rounded-lg bg-gray-100 object-cover" />
          <div class="mt-4 grid grid-cols-2 gap-4 sm:mt-6 sm:gap-6 lg:mt-8 lg:gap-8">
            <img src="/plus-assets/img/ecommerce-images/product-feature-09-detail-01.jpg" alt="Detail of temperature setting button on kettle bass with digital degree readout." class="aspect-square w-full rounded-lg bg-gray-100 object-cover" />
            <img src="/plus-assets/img/ecommerce-images/product-feature-09-detail-02.jpg" alt="Kettle spout pouring boiling water into coffee grounds in pour-over mug." class="aspect-square w-full rounded-lg bg-gray-100 object-cover" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const features = [
  {
    name: 'Sleek design',
    description:
      'The machined kettle has a smooth black finish and contemporary shape that stands apart from most plastic appliances.',
  },
  { name: 'Comfort handle', description: 'Shaped for steady pours and insulated to prevent burns.' },
  {
    name: 'One-button control',
    description:
      'The one button control has a digital readout for setting temperature and turning the kettle on and off.',
  },
  { name: 'Long spout', description: "Designed specifically for controlled pour-overs that don't slash or sputter." },
]
</script>
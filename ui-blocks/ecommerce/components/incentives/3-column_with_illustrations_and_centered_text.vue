<template>
  <div class="bg-gray-50">
    <div class="mx-auto max-w-7xl py-24 sm:px-2 sm:py-32 lg:px-4">
      <div class="mx-auto grid max-w-2xl grid-cols-1 gap-x-8 gap-y-10 px-4 lg:max-w-none lg:grid-cols-3">
        <div v-for="incentive in incentives" :key="incentive.name" class="text-center sm:flex sm:text-left lg:block lg:text-center">
          <div class="sm:shrink-0">
            <div class="flow-root">
              <img class="mx-auto h-24 w-28" :src="incentive.imageSrc" alt="" />
            </div>
          </div>
          <div class="mt-3 sm:mt-0 sm:ml-3 lg:mt-3 lg:ml-0">
            <h3 class="text-sm font-medium text-gray-900">{{ incentive.name }}</h3>
            <p class="mt-2 text-sm text-gray-500">{{ incentive.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const incentives = [
  {
    name: 'Free Shipping',
    description: "It's not actually free we just price it into the products. Someone's paying for it, and it's not us.",
    imageSrc: '/plus-assets/img/ecommerce/icons/icon-delivery-light.svg',
  },
  {
    name: '24/7 Customer Support',
    description: 'Our AI chat widget is powered by a naive series of if/else statements. Guaranteed to irritate.',
    imageSrc: '/plus-assets/img/ecommerce/icons/icon-chat-light.svg',
  },
  {
    name: 'Fast Shopping Cart',
    description: "Look how fast that cart is going. What does this mean for the actual experience? I don't know.",
    imageSrc: '/plus-assets/img/ecommerce/icons/icon-fast-checkout-light.svg',
  },
]
</script>
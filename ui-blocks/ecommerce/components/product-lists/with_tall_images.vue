<template>
  <div class="bg-white">
    <div class="mx-auto max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8">
      <h2 id="products-heading" class="sr-only">Products</h2>

      <div class="grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-3 xl:gap-x-8">
        <a v-for="product in products" :key="product.id" :href="product.href" class="group">
          <img :src="product.imageSrc" :alt="product.imageAlt" class="aspect-square w-full overflow-hidden rounded-lg object-cover group-hover:opacity-75 sm:aspect-2/3" />
          <div class="mt-4 flex items-center justify-between text-base font-medium text-gray-900">
            <h3>{{ product.name }}</h3>
            <p>{{ product.price }}</p>
          </div>
          <p class="mt-1 text-sm text-gray-500 italic">{{ product.description }}</p>
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
const products = [
  {
    id: 1,
    name: 'Focus Paper Refill',
    href: '#',
    price: '$13',
    description: '3 sizes available',
    imageSrc: '/plus-assets/img/ecommerce-images/category-page-01-image-card-01.jpg',
    imageAlt: 'Person using a pen to cross a task off a productivity paper card.',
  },
  {
    id: 2,
    name: 'Focus Card Holder',
    href: '#',
    price: '$64',
    description: 'Walnut',
    imageSrc: '/plus-assets/img/ecommerce-images/category-page-01-image-card-02.jpg',
    imageAlt: 'Paper card sitting upright in walnut card holder on desk.',
  },
  {
    id: 3,
    name: 'Focus Carry Case',
    href: '#',
    price: '$32',
    description: 'Heather Gray',
    imageSrc: '/plus-assets/img/ecommerce-images/category-page-01-image-card-03.jpg',
    imageAlt: 'Textured gray felt pouch for paper cards with snap button flap and elastic pen holder loop.',
  },
  // More products...
]
</script>
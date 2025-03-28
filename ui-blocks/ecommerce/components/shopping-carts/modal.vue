<template>
  <TransitionRoot as="template" :show="open">
    <Dialog class="relative z-10" @close="open = false">
      <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100" leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
        <div class="hidden sm:fixed sm:inset-0 sm:block sm:bg-gray-500/75 sm:transition-opacity" />
      </TransitionChild>

      <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
        <div class="flex min-h-full items-stretch justify-center text-center sm:items-center sm:px-6 lg:px-8">
          <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0 scale-105" enter-to="opacity-100 scale-100" leave="ease-in duration-200" leave-from="opacity-100 scale-100" leave-to="opacity-0 scale-105">
            <DialogPanel class="flex w-full max-w-3xl transform text-left text-base transition sm:my-8">
              <form class="relative flex w-full flex-col overflow-hidden bg-white pt-6 pb-8 sm:rounded-lg sm:pb-6 lg:py-8">
                <div class="flex items-center justify-between px-4 sm:px-6 lg:px-8">
                  <h2 class="text-lg font-medium text-gray-900">Shopping Cart</h2>
                  <button type="button" class="text-gray-400 hover:text-gray-500" @click="open = false">
                    <span class="sr-only">Close</span>
                    <XMarkIcon class="size-6" aria-hidden="true" />
                  </button>
                </div>

                <section aria-labelledby="cart-heading">
                  <h2 id="cart-heading" class="sr-only">Items in your shopping cart</h2>

                  <ul role="list" class="divide-y divide-gray-200 px-4 sm:px-6 lg:px-8">
                    <li v-for="(product, productIdx) in products" :key="product.id" class="flex py-8 text-sm sm:items-center">
                      <img :src="product.imageSrc" :alt="product.imageAlt" class="size-24 flex-none rounded-lg border border-gray-200 sm:size-32" />
                      <div class="ml-4 grid flex-auto grid-cols-1 grid-rows-1 items-start gap-x-5 gap-y-3 sm:ml-6 sm:flex sm:items-center sm:gap-0">
                        <div class="row-end-1 flex-auto sm:pr-6">
                          <h3 class="font-medium text-gray-900">
                            <a :href="product.href">{{ product.name }}</a>
                          </h3>
                          <p class="mt-1 text-gray-500">{{ product.color }}</p>
                        </div>
                        <p class="row-span-2 row-end-2 font-medium text-gray-900 sm:order-1 sm:ml-6 sm:w-1/3 sm:flex-none sm:text-right">{{ product.price }}</p>
                        <div class="flex items-center sm:block sm:flex-none sm:text-center">
                          <div class="inline-grid w-full max-w-16 grid-cols-1">
                            <select :name="`quantity-${productIdx}`" :aria-label="`Quantity, ${product.name}`" class="col-start-1 row-start-1 appearance-none rounded-md bg-white py-1.5 pr-8 pl-3 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6">
                              <option value="1">1</option>
                              <option value="2">2</option>
                              <option value="3">3</option>
                              <option value="4">4</option>
                              <option value="5">5</option>
                              <option value="6">6</option>
                              <option value="7">7</option>
                              <option value="8">8</option>
                            </select>
                            <ChevronDownIcon class="pointer-events-none col-start-1 row-start-1 mr-2 size-5 self-center justify-self-end text-gray-500 sm:size-4" aria-hidden="true" />
                          </div>

                          <button type="button" class="ml-4 font-medium text-indigo-600 hover:text-indigo-500 sm:mt-2 sm:ml-0">
                            <span>Remove</span>
                          </button>
                        </div>
                      </div>
                    </li>
                  </ul>
                </section>

                <section aria-labelledby="summary-heading" class="mt-auto sm:px-6 lg:px-8">
                  <div class="bg-gray-50 p-6 sm:rounded-lg sm:p-8">
                    <h2 id="summary-heading" class="sr-only">Order summary</h2>

                    <div class="flow-root">
                      <dl class="-my-4 divide-y divide-gray-200 text-sm">
                        <div class="flex items-center justify-between py-4">
                          <dt class="text-gray-600">Subtotal</dt>
                          <dd class="font-medium text-gray-900">$262.00</dd>
                        </div>
                        <div class="flex items-center justify-between py-4">
                          <dt class="text-gray-600">Shipping</dt>
                          <dd class="font-medium text-gray-900">$5.00</dd>
                        </div>
                        <div class="flex items-center justify-between py-4">
                          <dt class="text-gray-600">Tax</dt>
                          <dd class="font-medium text-gray-900">$53.40</dd>
                        </div>
                        <div class="flex items-center justify-between py-4">
                          <dt class="text-base font-medium text-gray-900">Order total</dt>
                          <dd class="text-base font-medium text-gray-900">$320.40</dd>
                        </div>
                      </dl>
                    </div>
                  </div>
                </section>

                <div class="mt-8 flex justify-end px-4 sm:px-6 lg:px-8">
                  <button type="submit" class="rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-xs hover:bg-indigo-700 focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:ring-offset-gray-50 focus:outline-hidden">Continue to Payment</button>
                </div>
              </form>
            </DialogPanel>
          </TransitionChild>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>

<script setup>
import { ref } from 'vue'
import { Dialog, DialogPanel, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { XMarkIcon } from '@heroicons/vue/24/outline'
import { ChevronDownIcon } from '@heroicons/vue/16/solid'

const products = [
  {
    id: 1,
    name: 'Zip Tote Basket',
    href: '#',
    color: 'White and black',
    price: '$140.00',
    imageSrc: '/plus-assets/img/ecommerce-images/shopping-cart-page-04-product-03.jpg',
    imageAlt: 'Front of zip tote bag with white canvas, black canvas straps and handle, and black zipper pulls.',
  },
  {
    id: 2,
    name: 'Throwback Hip Bag',
    href: '#',
    color: 'Salmon',
    price: '$90.00',
    imageSrc: '/plus-assets/img/ecommerce-images/shopping-cart-page-04-product-01.jpg',
    imageAlt: 'Salmon orange fabric pouch with match zipper, gray zipper pull, and adjustable hip belt.',
  },
  // More products...
]

const open = ref(true)
</script>
<template>
  <div>
    <h2>Zoznam objednávok</h2>
    <div v-if="orders.length">
      <ul>
        <OrderItem v-for="order in orders" :key="order.id" :order="order" />
      </ul>
    </div>
    <div v-else>
      Načítavam objednávky...
    </div>
  </div>
</template>

<script setup lang="ts">

import OrderItem from '../components/OrderItem.vue'
import { ref, onMounted } from 'vue'
import { getOrders } from '../services/orderService'

interface Order {
  id: number
  order_number: string
  customer_name: string
  date: string
}

const orders = ref<Order[]>([])

onMounted(async () => {
  try {
    const response = await getOrders()
    orders.value = response.data
  } catch (error) {
    console.error('Chyba pri načítaní objednávok:', error)
  }
})

</script>

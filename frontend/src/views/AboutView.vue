<template>
  <div class="about">
    <h1>This is an about page</h1>
    <div v-if="orders.length">
      <div v-for="order in orders" :key="order.id">
        {{ order.order_number }} - {{ order.customer_name }} - {{ order.date }}
      </div>
    </div>
    <div v-else>
      Loading orders...
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getOrders } from '@/services/orderService'

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
    console.error('Error loading orders:', error)
  }
})
</script>
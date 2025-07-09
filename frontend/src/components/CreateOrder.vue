<template>
  <div>
    <h2>Create Order</h2>
    <form @submit.prevent="submitOrder">
      <div>
        <label>Order Number:</label>
        <input v-model="order_number" required />
      </div>
      <div>
        <label>Customer Name:</label>
        <input v-model="customer_name" required />
      </div>
      <div>
        <DateInput v-model="date" label="Select Date" />
      </div>
      <button type="submit">Create</button>
    </form>
    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script setup lang="ts">

import DateInput from './inputs/DatePicker.vue'
import { ref } from 'vue'
import { createOrder } from '../services/orderService'

const order_number = ref('')
const customer_name = ref('')
const date = ref('')
const message = ref('')

const submitOrder = async () => {
  try {
    await createOrder({
      order_number: order_number.value,
      customer_name: customer_name.value,
      date: date.value
    })
    message.value = 'Order created successfully!'
    order_number.value = ''
    customer_name.value = ''
    date.value = ''
  } catch (error) {
    console.error(error)
    message.value = 'Error creating order.'
  }
}
</script>
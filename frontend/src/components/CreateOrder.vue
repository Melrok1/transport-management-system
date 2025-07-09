<template>
  <div class="create-order--container">
    <h2>Vytvoriť objednávku</h2>
    <form @submit.prevent="submitOrder">
      <div>
        <label>Číslo objednávky:</label>
        <input v-model="order_number" required />
      </div>
      <div>
        <label>Meno zákazníka:</label>
        <input v-model="customer_name" required />
      </div>
      <div>
        <DateInput v-model="date" label="Dátum:" />
      </div>
      <button type="submit">Vytvor objednávku</button>
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

<style scoped lang="scss">

.create-order--container {
  max-width: 400px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f9f9f9;

  h2 {
    text-align: center;
    margin-bottom: 20px;
  }

  form {
    display: flex;
    flex-direction: column;

    div {
      margin-bottom: 15px;

      label {
        display: block;
        margin-bottom: 5px;
      }

      input {
        width: 100%;
        padding: 8px;
        box-sizing: border-box;
      }
    }

    button {
      padding: 10px;
      background-color: #28a745;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;

      &:hover {
        background-color: #218838;
      }
    }
  }

  p {
    text-align: center;
    color: green;
    margin-top: 15px;
  }
}

</style>

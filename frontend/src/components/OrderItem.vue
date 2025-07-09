<template>
  <li class="order-item">
    {{ order.order_number }} – {{ order.customer_name }} – {{ order.date }}
  </li>
</template>

<script setup lang="ts">

import { defineProps } from 'vue'

interface Order {
  id: number
  order_number: string
  customer_name: string
  date: string
}

const props = defineProps<{
  order: Order
}>()

</script>

<style scoped lang="scss">

.order-item {
	padding: 10px;
	border-bottom: 1px solid #ccc;
	list-style-type: none;
	font-size: 16px;
	color: #333;

	&:hover {
		background-color: #f9f9f9;
		cursor: pointer;
	}
}

</style>

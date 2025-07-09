<template>
  <li @click="goToDetail" class="order-item">
		<div class="item-wrapper">
			<div>
				<span class="label">číslo objednávky:</span>
				<span>{{ order.order_number }}</span>
			</div>
			<div>
				<span class="label">meno zákazníka:</span>
				<span>{{ order.customer_name }}</span>
			</div>
			<div>
				<span class="label">dátum:</span>
				<span>{{ order.date }}</span>
			</div>
		</div>
		<div v-if="order.waypoints.length">
			<h4>Body trasy (Zastávky)</h4>
			<ul>
				<li v-for="waypoint in order.waypoints" :key="waypoint.id" class="waypoint-item">
					<span>
						{{ waypoint.location }} ({{ waypoint.waypoint_type }})	
					</span>
				</li>
			</ul>
		</div>
  </li>
</template>

<script setup lang="ts">

import { defineProps } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

interface Order {
  id: number
  order_number: string
  customer_name: string
  date: string
	waypoints: Array<{
		id: number
		order: number
		location: string
		waypoint_type: string
	}>
}

const props = defineProps<{
  order: Order
}>()

const goToDetail = () => {
  router.push(`/orders/${props.order.id}`)
}

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

.item-wrapper {
	display: flex;
	flex-direction: column;
	align-items: flex-start;
}

.label {
	font-weight: bold;
	margin-right: 1rem;
}

.waypoint-item {
	list-style-type: none;
	padding: 5px 0;

	span::before {
		content: '• ';
		color: #007bff;
	}
}

</style>

<template>
  <div class="order-detail">
    <header>
			<h2>Detail objednávky</h2>
			<button @click="goBack">← Späť na zoznam</button>
    </header>

    <div v-if="loading">Načítavam...</div>
    <div v-else-if="order">
      <p><strong>Číslo objednávky:</strong> {{ order.order_number }}</p>
      <p><strong>Meno zákazníka:</strong> {{ order.customer_name }}</p>
      <p><strong>Dátum:</strong> {{ order.date }}</p>

			<div class="waypoints-list">
				<h3>Zastávky (Waypoints)</h3>
				<ul>
					<li v-for="waypoint in order.waypoints" :key="waypoint.id">
						{{ waypoint.location }} ({{ waypoint.waypoint_type }})
					</li>
				</ul>
			</div>

      <div class="add-waypoint">
        <h4>Pridať zastávku</h4>
        <form @submit.prevent="addWaypoint">
          <input v-model="newWaypointLocation" placeholder="Lokácia" required />
          <select v-model="newWaypointType" required>
            <option disabled value="">Vyber typ</option>
            <option value="pickup">Pickup</option>
            <option value="delivery">Delivery</option>
          </select>
          <button type="submit">Pridať</button>
        </form>
      </div>
    </div>
    <div v-else>
      <p>Objednávka sa nenašla.</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getOrderById } from '@/services/orderService'
import { createWaypoint } from '@/services/waypointService'

const route = useRoute()
const router = useRouter()

const order = ref<any>(null)
const loading = ref(true)
const newWaypointLocation = ref('')
const newWaypointType = ref('')

const fetchOrder = async () => {
  try {
    const response = await getOrderById(Number(route.params.id))
    order.value = response.data
  } catch (error) {
    console.error('Error fetching order:', error)
  } finally {
    loading.value = false
  }
}

const addWaypoint = async () => {
  if (!newWaypointLocation.value || !newWaypointType.value) return

  try {
    await createWaypoint({
      order: order.value.id,
      location: newWaypointLocation.value,
      waypoint_type: newWaypointType.value
    })
    await fetchOrder()
    newWaypointLocation.value = ''
    newWaypointType.value = ''
  } catch (error) {
    console.error('Error adding waypoint:', error)
  }
}

const goBack = () => {
  router.push('/ordersListView')
}

onMounted(() => {
  fetchOrder()
})
</script>

<style scoped lang="scss">

header {
	display: flex;
	justify-content: space-between;
	align-items: center;
	border-bottom: 1px solid rgba(66, 185, 131, 0.5);
	margin-bottom: 20px;

	h2 {
		margin: 0 0 1rem 0;
	}

	button {
		padding: 10px;
		background-color: #42b983;
		color: white;
		border: none;
		border-radius: 5px;
		margin-bottom: 1rem;
		cursor: pointer;
	}
}

.order-detail {
  max-width: 600px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f9f9f9;

  h2, h3, h4 {
    margin-top: 0;
  }

	.waypoints-list {
		margin-bottom: 20px;
		padding-top: 1rem;
		border-top: 1px solid rgba(66, 185, 131, 0.5);

		ul {
			list-style-type: none;
			padding: 0;

			li {
				padding: 5px 0;
			}
		}
	}	

	.add-waypoint {
		padding-top: 1rem;
		border-top: 1px solid rgba(66, 185, 131, 0.5);
	}

  form {
    display: flex;
    flex-direction: column;

    input, select {
      margin-bottom: 10px;
      padding: 8px;
      border-radius: 4px;
      border: 1px solid #ccc;
    }

    button[type="submit"] {
      background-color: #42b983;
      color: white;
      border: none;
      padding: 10px;
      cursor: pointer;
    }
  }
}
</style>

import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000/api/',
})

// GET all orders
export const getOrders = () => {
  return api.get('orders/')
}

// POST create order
export const createOrder = (data: {
  order_number: string
  customer_name: string
  date: string
}) => {
  return api.post('orders/', data)
}

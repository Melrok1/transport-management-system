import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000/api/',
})

// POST create waypoint
export const createWaypoint = (data: {
  order: number
  location: string
  waypoint_type: string
}) => {
  return api.post('waypoints/', data)
}

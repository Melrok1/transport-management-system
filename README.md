# 🚛 Transport Management System

## 💡 Project Description
A simple full-stack logistics order management system built with **Vue.js + TypeScript** (frontend) and **Django REST Framework** (backend).  
Users can create transport orders with multiple waypoints (pickup/delivery stops) and view them in an organized list.

---

## ⚙️ Features
- ✅ Create transport orders (order number, customer name, date)
- ✅ Assign multiple waypoints (location, type) to each order
- ✅ View detailed order information with all waypoints
- ✅ Minimalistic, functional UI with Composition API

---

## 🛠️ Tech Stack

### 🔷 Frontend
- Vue.js 3
- TypeScript
- Axios
- Vue Router

### 🔶 Backend
- Python 3.13.5
- Django 5.2
- Django REST Framework
- django-cors-headers

---

## 🚀 Installation & Setup

### 1. Clone the repository
```sh
git clone https://github.com/Melrok1/transport-management-system
```

### 2. Backend Setup
```sh
cd transport-management-system/backend
python -m venv venv
```
**Activate virtual environment:**
- Windows PowerShell:
  ```sh
  .\venv\Scripts\Activate
  ```
- Git Bash:
  ```sh
  source venv/Scripts/activate
  ```

**Install dependencies:**
```sh
pip install -r requirements.txt
```

**Run migrations:**
```sh
python manage.py makemigrations
python manage.py migrate
```

**Start the backend server:**
```sh
python manage.py runserver
```

### 3. Frontend Setup
```sh
cd transport-management-system/frontend
npm install
npm run serve
```

---

## 🔗 API Endpoints

| Method | URL                  | Description                    |
|--------|----------------------|--------------------------------|
| GET    | /api/orders/         | List all orders                |
| POST   | /api/orders/         | Create a new order             |
| GET    | /api/orders/:id/     | Retrieve order details by ID   |
| POST   | /api/waypoints/      | Create a new waypoint          |

---

## 📝 Assumptions & Decisions
- Frontend built with Composition API as required by assignment.
- Waypoints are added to orders in detail view after order creation.
- UI kept minimalistic focusing on functionality, not design.
- Axios used for all API communication.

---

🔧 Possible Future Improvements:

Implement filtering orders by date or customer name in frontend list view.

Add edit and delete functionality for orders and waypoints.

Improve form validation and error handling for better UX.

Enhance UI with a responsive design framework.

Implement authentication for secure order management access.

Add pagination to the orders list for performance on large datasets.

Enable creating orders with nested waypoints in a single request.

🐞 Known Issues:

No filtering functionality implemented yet for orders list.

No input validation beyond basic HTML required fields.

Current CORS configuration allows all origins – adjust for production.

Limited error messages shown to the user; backend errors are logged only in console.

## ✍️ Author

Martin Blaščák  
09/07/2025 (DD/MM/YYYY)
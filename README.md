# 📅 School Scheduler

A web-based **school timetable generator** that automatically assigns courses to time slots while respecting real-world constraints such as teacher availability, classroom conflicts, and weekly lesson requirements.
![alt text](image-1.png)
---

## 🚀 Features

### ✅ Core Scheduling Constraints
- Teachers can only be assigned to their **available time slots**
- A teacher **cannot teach multiple classes at the same time**
- A class group **cannot have overlapping lessons**
- Each course must be scheduled according to its **weekly required hours**

---

### 🧠 Smart Scheduling Logic
- Automatically generates schedules using a constraint-aware algorithm
- Detects and reports **unsatisfied course hours (conflicts)**
- Supports **multiple classes (full school scheduling)**

---

### 📊 Interactive UI
- Clean **grid view grouped by class (10A, 10B, etc.)**
- Each lesson card shows:
  - Course name
  - Teacher
  - Class
- Highlights conflicts clearly
- One-click **Generate Schedule** button

---

## 🏗️ Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- SQLite
- Custom scheduling algorithm

### Frontend
- Next.js (React)
- Axios
- Simple responsive UI

---

## 📂 Project Structure

school-scheduler/
│
├── backend/
│   ├── app/
│   │   ├── api/routes/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── scheduler/
│   │   └── db/
│
├── frontend/
│   └── app/
│
└── README.md

---

## ⚙️ Setup & Run

### 1. Clone

```bash
git clone https://github.com/your-username/school-scheduler.git
cd school-scheduler
```

---

### 2. Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

Swagger:
```
http://127.0.0.1:8000/docs
```

---

### 3. Frontend

```bash
cd frontend
npm install
npm run dev
```

App:
```
http://localhost:3000
```

---

## 🧪 Example Data

### Teacher

```json
{
  "name": "Ahmet",
  "available_slots": [1,2,3,4]
}
```

### Class

```json
{
  "name": "10A"
}
```

### Course

```json
{
  "name": "Physics",
  "teacher_id": 1,
  "class_id": 1,
  "weekly_hours": 2
}
```

---

## 🔄 API Endpoints

POST /teachers/ → create teacher  
POST /class-groups/ → create class  
POST /courses/ → create course  
POST /timeslots/ → create time slot  
POST /schedule/generate → generate schedule  
GET  /schedule/grid → get schedule grid  

---

## ⚠️ Conflict Example

```json
{
  "conflicts": [
    {
      "course": "Physics",
      "assigned": 1,
      "required": 2
    }
  ]
}
```

This means the system could not fully schedule the course due to constraints.

---

## 🎯 Future Improvements

- Better scheduling algorithm (backtracking / optimization)
- Teacher-based schedule view
- Drag & drop UI
- Export as PDF / Excel
- Conflict visualization

---

## 👨‍💻 Notes

This project simulates a real-world school scheduling system with:
- Constraint satisfaction
- Backend-heavy logic
- Interactive frontend

---
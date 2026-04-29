# 📅 School Scheduler

A web-based **school timetable generator** that automatically assigns courses to time slots while respecting real-world constraints such as teacher availability, classroom conflicts, and weekly lesson requirements.

---

## 🚀 Features

### ✅ Core Constraints
- Teachers can only be assigned to their **available time slots**
- A teacher **cannot teach multiple classes at the same time**
- A class group **cannot have overlapping lessons**
- Courses are scheduled based on **weekly required hours**

---

### 🧠 Scheduling Engine
- Constraint-based scheduling algorithm
- Handles **multi-class school planning**
- Detects and reports **conflicts automatically**

---

### 📊 UI Highlights
- Clean **grid-based timetable view**
- Organized by class (e.g., 10A, 10B)
- Each lesson shows:
  - Course name
  - Teacher
  - Class
- Conflict alerts displayed clearly

---

## 🖼️ Demo

```
![Demo](image.png)
```

---

## 🏗️ Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- SQLite
- Custom Scheduling Algorithm

### Frontend
- Next.js (React)
- Axios
- Tailwind / Custom Styling

---

## 📂 Project Structure

```
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
│   ├── app/
│   ├── public/
│   └── package.json
│
└── README.md
```

---

## ⚙️ Setup & Run

### 1. Clone

```bash
git clone https://github.com/emredogan123/school-scheduler.git
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

Swagger Docs:
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

## 🧪 Example API Usage

### Create Teacher

```json
{
  "name": "Ahmet",
  "available_slots": [1,2,3,4]
}
```

---

### Create Class

```json
{
  "name": "10A"
}
```

---

### Create Course

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

| Method | Endpoint | Description |
|------|--------|------------|
| POST | `/teachers/` | Create teacher |
| POST | `/class-groups/` | Create class |
| POST | `/courses/` | Create course |
| POST | `/timeslots/` | Create time slot |
| POST | `/schedule/generate` | Generate schedule |
| GET  | `/schedule/grid` | Get schedule grid |

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

---

## 🎯 Future Improvements

- Advanced scheduling (backtracking / optimization)
- Teacher-based timetable view
- Drag & drop UI
- Export to PDF / Excel
- Conflict visualization improvements

---

## 👨‍💻 About

This project demonstrates:
- Constraint-based problem solving
- Backend-heavy architecture
- Full-stack development (FastAPI + React)

---

## ⭐ Notes

> node_modules, venv, and build files are excluded via `.gitignore`.

---

## 📌 Author

Developed by **Emre Doğan**
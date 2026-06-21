# 💰 Expense AI Tracker

An AI-powered Expense Tracking & Budget Management System built with **FastAPI, React, and Supabase**. The application helps users manage income and expenses, monitor spending habits, set financial goals, and gain insights through interactive dashboards.

---

## 🚀 Features

### 🔐 User Authentication

* User Registration
* User Login
* Secure Password Hashing
* JWT-based Authentication

### 💸 Expense Management

* Add Expenses
* Categorize Transactions
* Track Spending History
* Filter Expenses by Category and Date

### 💵 Income Management

* Add Income Sources
* Monitor Monthly Income
* Compare Income vs Expenses

### 📊 Dashboard & Analytics

* Total Income Overview
* Total Expense Overview
* Balance Calculation
* Monthly Performance Tracking
* Category-wise Expense Analysis
* Recent Transactions

### 🎯 Goal Tracking

* Create Savings Goals
* Track Goal Progress
* Visual Progress Indicators

### 🤖 AI Insights

* Spending Pattern Analysis
* Budget Recommendations
* Financial Suggestions
* Smart Expense Monitoring

---

## 🛠️ Tech Stack

### Frontend

* Javascript
* HTML
* CSS / Tailwind CSS

### Backend

* FastAPI
* Python
* JWT Authentication
* Pydantic

### Database

* Supabase PostgreSQL
---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/dhanshree-creator/Expense-AI-Tracker.git
cd Expense-AI-Tracker
```

### 2. Backend Setup

```bash
cd backend

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

Start Backend:

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

### 3. Frontend Setup

```bash
cd frontend

npm install
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

## 🗄️ Database Setup

Run the provided SQL schema in Supabase SQL Editor.

Tables:

* users
* expenses
* income

The database uses UUID-based primary keys and foreign key relationships for secure data management.

---

## 📈 Dashboard Metrics

* Total Income
* Total Expenses
* Current Balance
* Monthly Spending Trends
* Goal Progress Tracking
* Expense Distribution

---

## 🔒 Security

* Password Hashing
* JWT Authentication
* Protected API Endpoints
* Row-Level Security (RLS) Enabled in Supabase
* Environment Variables for Sensitive Data

---

## 🎯 Future Enhancements

* AI Expense Forecasting
* Export Reports (PDF/Excel)
* Email Notifications
* Multi-Currency Support
* Recurring Transactions
* Mobile Application
* Advanced Financial Analytics

---

## 👩‍💻 Author

**Dhanshree**

GitHub:
https://github.com/dhanshree-creator

---

## 📄 License

This project is developed for educational and portfolio purposes.

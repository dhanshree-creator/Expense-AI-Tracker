# Smart Expense Tracker  — Smart Wallet 

This is the upgraded version of your **FastAPI + Supabase + JWT** expense tracker.

## What is upgraded

- New Smart Wallet style dashboard inspired by your screenshot
- Financial health score gauge out of 1000
- Safe daily spending calculation
- Top expense card
- Recent combined transactions: income + expenses together
- Better donut chart for category spending
- Monthly income vs expense vs savings chart
- Money insights panel with real warnings
- Goals progress panel
- Monthly category budgets with overspending alerts
- Settings page with profile update, dark mode, monthly savings target, logout, reset local data, and delete account
- Better expense/income tables with search, filters, summaries and CSV export
- Backend endpoints added:
  - `PUT /auth/profile`
  - `DELETE /auth/account`
  - `GET /reports/health`
  - `GET /reports/recent-transactions`
  - `GET /reports/category-breakdown?period=current_month`

## Fast start

1. Run `docs/database.sql` in Supabase SQL Editor.
2. Copy `backend/.env.example` to `backend/.env` and add your Supabase Project URL + service role key.
3. Run:

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

4. Open:

```text
http://127.0.0.1:8000
```

## Important

Goals, budgets, dark mode and monthly savings target are stored in browser `localStorage`, so they work without extra Supabase tables. Income and expenses are still stored in Supabase and protected by JWT.

For project submission, this is actually a good architecture choice: core financial records are database-backed, while dashboard preferences remain lightweight.

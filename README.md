# 📝 TODO-List (Django Practice Project)

This project is a simple Todo List application built using **Django**.  
It allows users to create tasks, assign tags, set deadlines, and manage their progress.

---

## 🚀 Features

### ✔️ Task management
- Create, update, and delete tasks
- Mark tasks as **Done / Not done**
- Optional deadline for tasks
- Automatic task creation datetime
- Each task can have multiple tags

### 🏷️ Tag system
- Create, update, and delete tags
- Tags can be attached to multiple tasks


## 🏁 How to run locally

```bash
git clone https://github.com/Alexandr-Gluschenko/TODO-List.git
cd TODO-List
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

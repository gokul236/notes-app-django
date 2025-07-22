# Django Notes App

A clean, minimal **Notes Application** built using **Django**, allowing users to create, view, update, and delete notes with a category system.

## Features

✅ Create, edit, and delete notes  
✅ Categorize notes easily  
✅ View detailed note pages  
✅ Confirmation before deleting notes  
✅ Organized, clean Bootstrap-styled templates  
✅ Uses SQLite for lightweight local storage  
✅ Structured for easy further extension

## Screenshots

_Add screenshots here if needed (e.g., homepage, create note page, note list view)._

## Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/notes-app.git
cd notes-app/notesproject
```

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install django
```

Or if you have a `requirements.txt`, use:

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run the Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser to access the Notes App.

---

## Project Structure

```
notesproject/
│
├── db.sqlite3
├── manage.py
├── notes/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│       └── notes/
│           ├── category_form.html
│           ├── note_confirm_delete.html
│           ├── note_detail.html
│           ├── note_form.html
│           └── note_list.html
│   └── migrations/
└── notesproject/
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    └── asgi.py
```

---

## Technologies Used

- **Python 3**
- **Django**
- **SQLite** (default database)
- **Bootstrap** for styling

---

## Future Improvements

- User authentication (login/register)  
- Rich text editor for notes (CKEditor)  
- Search and filter notes  
- API support for mobile integration (Django REST Framework)

---

## Contributing

Pull requests are welcome. Please open an issue to discuss your proposed changes before submitting.

---

## License

This project is licensed under the [MIT License](LICENSE).

# Django MongoDB Authentication Backend

This project implements a backend authentication system using **Django** and **MongoDB Atlas**.
It demonstrates how to build custom user authentication with secure password hashing and session management without using Django’s default SQL-based ORM.

---

## 🚀 Features

* User Signup & Login
* Password hashing (secure storage)
* MongoDB Atlas integration using PyMongo
* Session-based authentication
* Custom authentication flow
* Clean project structure
* Styled UI pages (Home, Login, Signup, Dashboard)

---

## 🛠 Tech Stack

* **Backend:** Django (Python)
* **Database:** MongoDB Atlas (NoSQL)
* **Driver:** PyMongo
* **Authentication:** Custom logic with hashed passwords
* **Frontend:** HTML, CSS
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
databaseConnection/
├── authentication/        # Authentication app (views, urls)
├── databaseConnection/    # Project settings, urls, mongo config
├── templates/             # HTML templates
├── static/                # CSS files
├── manage.py
└── requirements.txt
```

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/KoranneVaidehi/django-mongo-authentication.git
cd django-mongo-authentication
```

### 2️⃣ Create & activate virtual environment

```bash
python -m venv env
env\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure MongoDB Atlas

* Create a MongoDB Atlas cluster
* Get the connection string
* Update it inside `databaseConnection/mongo.py`
* Make sure your IP is whitelisted in Atlas

### 5️⃣ Run the server

```bash
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```

---

## 🔐 Security Notes

* Passwords are **hashed** before storing in MongoDB
* Sensitive files are excluded using `.gitignore`
* MongoDB credentials should be stored securely (environment variables recommended for production)

---

## 📌 Learning Outcomes

* Django project & app structure
* MongoDB Atlas integration
* Custom authentication logic
* Secure password handling
* GitHub workflow (init, commit, push)

---

## 👩‍💻 Author

**Vaidehi Koranne**

---

## ⭐ Future Enhancements

* JWT authentication
* Environment variable setup
* Video upload feature
* Role-based access control
* API-based authentication

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

from databaseConnection.mongo import users_collection

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        # Check if user exists
        if users_collection.find_one({"email": email}):
            return render(request, "signup.html", {
                "error": "User already exists"
            })

        hashed_password = make_password(password)

        users_collection.insert_one({
            "username": username,
            "email": email,
            "password": hashed_password
        })

        return redirect("login")

    return render(request, "signup.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = users_collection.find_one({"email": email})

        if not user:
            return render(request, "login.html", {
                "error": "User not found"
            })

        if not check_password(password, user["password"]):
            return render(request, "login.html", {
                "error": "Invalid password"
            })

        # Session set
        request.session["user_id"] = str(user["_id"])
        request.session["username"] = user["username"]

        return redirect("dashboard")

    return render(request, "login.html")

def logout_view(request):
    request.session.flush()
    return redirect("home")

def dashboard(request):
    username = request.session.get("username")

    if not username:
        return redirect("login")

    return render(request, "dashboard.html", {
        "username": username
    })

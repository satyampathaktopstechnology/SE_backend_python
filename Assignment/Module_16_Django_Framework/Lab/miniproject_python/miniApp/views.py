from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from miniApp.models import Patient, Appointment


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        u = authenticate(username=username, password=password)

        if u is None:
            return JsonResponse({"status": "error", "message": "Invalid Credential !!!"})
        else:
            login(request, u)
            return redirect("home")

    if request.user.is_authenticated:
        return redirect("home")

    return render(request, "login.html")


def home(request):
    return render(request, "home.html")


@login_required(login_url="login")
def user_profile(request):
    return render(request, "user_profile.html")


def user_logout(request):
    logout(request)
    return redirect("login")


def user_register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Username already exists"})

        u = User(username=username, first_name=name, email=email)
        u.set_password(password)
        u.save()

        return redirect("login")

    return render(request, "register.html")


def Check_username(request):
    check = request.GET.get("Checkuser")

    if not check:
        return JsonResponse({"status": "error", "message": "Username required"})

    if User.objects.filter(username=check).exists():
        return JsonResponse({"status": "error", "message": "Username already taken"})
    else:
        return JsonResponse({"status": "success", "message": "Username available"})


@login_required(login_url="login")
def delete_user(request):
    user = request.user
    logout(request)
    user.delete()
    return redirect("register")


# ------------------ PATIENTS ------------------

@login_required(login_url="login")
def patients(request):
    patient_list = Patient.objects.filter(user=request.user)
    return render(request, "patients.html", {"patients": patient_list})


@login_required(login_url="login")
def add_patient(request):
    if request.method == "POST":
        Patient.objects.create(
            user=request.user,
            name=request.POST.get("name"),
            age=request.POST.get("age"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            condition=request.POST.get("condition"),
        )
        return redirect("patients")

    return render(request, "add_patient.html")


# ------------------ APPOINTMENTS ------------------

@login_required(login_url="login")
def appointments(request):
    appointment_list = Appointment.objects.filter(user=request.user)
    return render(request, "appointments.html", {"appointments": appointment_list})


@login_required(login_url="login")
def book_appointment(request):
    patients = Patient.objects.filter(user=request.user)

    if request.method == "POST":
        patient_id = request.POST.get("patient")

        patient = get_object_or_404(Patient, id=patient_id, user=request.user)

        Appointment.objects.create(
            user=request.user,
            patient=patient,
            date=request.POST.get("date"),
            time=request.POST.get("time"),
            doctor=request.POST.get("doctor"),
            notes=request.POST.get("notes"),
        )

        return redirect("appointments")

    return render(request, "book_appointment.html", {"patients": patients})




@login_required(login_url="login")
def filter_appointments(request):
    status = request.GET.get("status")

    if status:
        appointments = Appointment.objects.filter(user=request.user, status=status)
    else:
        appointments = Appointment.objects.filter(user=request.user)

    return render(request, "ajax/appointment_list.html", {
        "appointments": appointments
    })
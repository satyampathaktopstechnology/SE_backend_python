from django.urls import path
from miniApp.views import *

urlpatterns = [
    path("", home, name="home"),

    # Auth
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", user_register, name="register"),

    # Profile
    path("profile/", user_profile, name="profile"),
    path("delete-user/", delete_user, name="delete_user"),

    # Patients
    path("patients/", patients, name="patients"),           # list page
    path("patients/add/", add_patient, name="add_patient"),

    # Appointments
    path("appointments/", appointments, name="appointments"),
    path("appointments/book/", book_appointment, name="book_appointment"),

    # AJAX
    path("availableuser/", Check_username, name="availableuser"),
    path("filter-appointments/", filter_appointments, name="filter_appointments"),
]
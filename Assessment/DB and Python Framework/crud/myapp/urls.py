from django.urls import path
from myapp.views import *


urlpatterns = [
    path("", home, name="home"),
    path("add-profile", add_profile, name="add-profile"),
    path("profile", add_profile, name="profile"),
    path("editpage", editpage, name="editpage"),
    path("delete", delete, name="delete"),
    path("export", export_csv, name="export"),
]
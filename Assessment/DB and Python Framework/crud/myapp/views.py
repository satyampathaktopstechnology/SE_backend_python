from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
import csv
from .models import Userprofile

def home(request):
    if request.method == "POST":
        uid = request.POST.get("id")
        # Handle Edit/Update
        if uid:
            p = Userprofile.objects.get(pk=uid)
            p.username = request.POST.get("username")
            p.email = request.POST.get("email")
            p.is_public = 'is_public' in request.POST
            p.save()
        return redirect("home")

    # Pagination logic
    user_list = Userprofile.objects.all().order_by('-id')
    paginator = Paginator(user_list, 5) # 5 users per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, "home.html", {"page_obj": page_obj})

def add_profile(request):
    if request.method == 'POST':
        data = request.POST
        Userprofile.objects.create(
            username=data.get("username"),
            email=data.get("email"),
            password=data.get("password"),
            is_public='is_public' in data
        )
        return redirect("home")
    return render(request, "add_profile.html")

def editpage(request):
    e = request.GET.get('id')
    user = Userprofile.objects.get(pk=e)
    return JsonResponse({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "is_public": user.is_public 
    })

def delete(request):
    d = request.GET.get("id")
    Userprofile.objects.get(pk=d).delete()
    return JsonResponse({"status":"Deleted Successfully"})

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Username', 'Email', 'Public'])
    users = Userprofile.objects.all()
    for user in users:
        writer.writerow([user.id, user.username, user.email, user.is_public])
    return response
from django.shortcuts import render

def profile_page(request):
    return render(request,"pages/dashboard.html")
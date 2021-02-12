from django.shortcuts import render
from .models import Slider_Images_Model,firstPageGridContent,firstPageGrid

def dashboard(request):
    return render(request,'dashboard-en/dashboard.html')
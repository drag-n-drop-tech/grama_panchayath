from django.shortcuts import render
from .models import Slider_Images_Model,firstPageGridContent,firstPageGrid

def dashboard(request):
    return render(request,'dashboard-en/dashboard.html')


def slider(request):
    return render(request, 'dashboard-en/slider.html')


def grid(request):
    return render(request, 'dashboard-en/grid.html')


def news(request):
    return render(request, 'dashboard-en/news.html')
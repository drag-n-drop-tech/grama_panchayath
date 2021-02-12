from django.shortcuts import render
from .models import Slider_Images_Model,firstPageGridContent,firstPageGrid, News



# Create your views here.
def  index(request):
    context = {}
    images = Slider_Images_Model.objects.all().order_by('Sequence')
    context['images'] = images
    context['grids'] = firstPageGrid.objects.all()
    context['gridContents'] = firstPageGridContent.objects.all()
    return render(request, 'website-kn/index.html', context)


def about_us(request):
    return render(request, 'website-kn/about-us.html')

def members(request):
    return render(request, 'website-kn/members.html')

def staffs(request):
    return render(request, 'website-kn/staff.html')

def property_info(request):
    return render(request, 'website-kn/property-info.html')

def education_info(request):
    return render(request, 'website-kn/education-info.html')

def visit_places(request):
    return render(request, 'website-kn/visit-places.html')

def library(request):
    return render(request, 'website-kn/library.html')

def others(request):
    context = {}
    news = News.objects.all()
    context['newses'] = news
    return render(request, 'website-kn/othres.html', context)
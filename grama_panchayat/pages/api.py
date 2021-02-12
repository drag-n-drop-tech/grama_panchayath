from rest_framework import viewsets, permissions
from .models import Slider_Images_Model, firstPageGrid, firstPageGridContent, News
from .serializer import imagesSerializer, gridSerializer, newsSerializer



class addImages(viewsets.ModelViewSet):
    queryset = Slider_Images_Model.objects.all()
    serializer_class = imagesSerializer


class GridViewset(viewsets.ModelViewSet):
    queryset = firstPageGrid.objects.all()
    serializer_class = gridSerializer

class newsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = newsSerializer
    permissions = [
        permissions.AllowAny
    ]
from rest_framework import serializers
from .models import Slider_Images_Model, firstPageGrid, News

class imagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider_Images_Model
        fields = '__all__'


class gridSerializer(serializers.ModelSerializer):
    class Meta:
        model = firstPageGrid
        fields = '__all__'

class newsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
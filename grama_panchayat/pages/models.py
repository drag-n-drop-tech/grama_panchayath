from django.db import models

# Create your models here.
def positiveNumber():
    return (Slider_Images_Model.objects.all().count() + 1)


class Slider_Images_Model(models.Model):
    Image = models.FileField(upload_to='')
    Sequence = models.PositiveIntegerField(default = positiveNumber)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField( auto_now=True)


class firstPageGrid(models.Model):
    Grid_Title = models.CharField(max_length = 255)
    content_moving = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    
class firstPageGridContent(models.Model):
    first_page_grid = models.ForeignKey( firstPageGrid, on_delete=models.CASCADE) 
    content = models.CharField(max_length = 255)
    content_type_is_link = models.BooleanField(default=False)
    isNew = models.BooleanField(default=False)
    url = models.CharField(max_length=50)

class News(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to="")
    short_description = models.CharField(max_length=255)
    detailed_description = models.TextField(null=True, blank=True)




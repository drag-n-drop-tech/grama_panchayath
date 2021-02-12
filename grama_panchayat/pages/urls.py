from django.urls import path, include
from rest_framework import routers
from . import views,dashboardViews
from .api import addImages, GridViewset, newsViewSet



router = routers.DefaultRouter()
router.register('add_slider', addImages, 'add_slider')
router.register('GridViewset', GridViewset, 'GridViewset')
router.register('newsViewSet', newsViewSet, 'newsViewSet')


urlpatterns = [
    ### apis ###
    path('api/', include(router.urls)),
    #######
    path('', views.index, name="index_page"),
    path('about-us', views.about_us, name="about_us"),
    path('members', views.members, name="members"),
    path('staffs', views.staffs, name="staffs"),
    path('property-info', views.property_info, name="property_info"),
    path('education-info', views.education_info, name="education_info"),
    path('visit-places', views.visit_places, name="visit_places"),
    path('library', views.library, name="library"),
    path('others', views.others, name="others"),

    #doshboard URLs

    path('dashboard',dashboardViews.dashboard,name="dashbaord"),
    path('slider',dashboardViews.slider,name="slider"),
    path('grid',dashboardViews.grid,name="grid"),
    path('news',dashboardViews.news,name="news"),
]

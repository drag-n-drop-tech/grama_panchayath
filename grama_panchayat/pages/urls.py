from django.urls import path, include

from . import views,dashboardViews

urlpatterns = [
    
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
]

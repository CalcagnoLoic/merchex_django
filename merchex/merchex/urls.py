from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', views.band_list, name="band-list"),
    path('bands/<int:id>/', views.band_detail, name="band-detail"),
    path('about-us/', views.about),
    path('contact-us', views.contact),
    path('annonces', views.listings_list, name='listings-list'),
    path('title/<int:id>/', views.listings_detail, name="listings-detail")

]

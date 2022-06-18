from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.band_list, name="band-list"),
    path('bands/<int:id>/', views.band_detail, name="band-detail"),
    path('bands/<int:id>/change/', views.band_change, name="band-change"),
    path('bands/<int:id>/delete/', views.band_delete, name="band-delete"),
    path('bands/add/', views.band_create, name="band-create"),
    path('about-us/', views.about, name="about"),
    path('contact-us', views.contact, name="contact"),
    path('annonces', views.listings_list, name='listings-list'),
    path('title/<int:id>/', views.listings_detail, name="listings-detail"),
    path('annonces/add/', views.listings_create, name="listings-create"),
    path('title/<int:id>/change/', views.listings_change, name='listings-change'),
    path('title/<int:id>/delete/', views.listings_delete, name='listings-delete'),
    path('email_sent.html', views.email_sent)

]

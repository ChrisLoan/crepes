from django.urls import include,re_path
from blog import views
from django.contrib import admin
from django.urls import path

app_name = "blog"

urlpatterns = [
    path('accueil/', views.accueil),
    path('article/<id>/' ,views.lire),
    path('date/',views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/',views.addition),
    path('caca/', views.caca),
    path('contact/',views.contact,name= 'contact')
]
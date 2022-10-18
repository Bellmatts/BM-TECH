from django.urls import path

from Site import views

app_name = "Site"
urlpatterns = [
    path('home', views.home, name='homepage')

]
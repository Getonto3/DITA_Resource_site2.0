from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage, name='home'),
    path('hardware/', views.Hardware, name='hardware'),
    path('software', views.Software, name='software'),
    path('tutor', views.Tutor, name='tutor'),
]
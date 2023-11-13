from django.urls import path
from . import views
from .views import Tutor,register, user_login,user_logout

urlpatterns = [
    path('', views.Homepage, name='homepage'),
    path('hardware/', views.Hardware, name='hardware'),
    path('software', views.Software, name='software'),
    path('tutor', Tutor, name='tutor'),
    path('register/',register,name='register'),
    path('login/', user_login, name='login'),
     path('logout/', user_logout, name='logout'),
    ]
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name='index'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('register', views.register,name='register'),
    path('post', views.register,name='post'),#idk why is it working but dont touch it
    path('logout',views.logout, name='logout')
]
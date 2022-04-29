from django.conf import settings
from . import views
from django.urls import path
from django.conf.urls.static import static

app_name = 'plancon'

urlpatterns = [
    path('', views.index,name='index'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('register', views.register,name='register'),
    path('addcon', views.addcon,name='addcon'),
    path('login', views.login_view,name='login'),
    path('post', views.register,name='post'),#idk why is it working but dont touch it
    path('logout',views.logout_view, name='logout')
]
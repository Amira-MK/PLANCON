from django.conf import settings
from django.views import View
from . import views
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'plancon'

urlpatterns = [
    path('', views.index,name='index'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('register', views.register,name='register'),
    path('addcon', views.addcon,name='addcon'),
    path('addarticle/<int:conf_id>/', views.addarticle,name='addarticle'),
    path('aboutconf/<int:conf_id>/', views.aboutconf,name='aboutconf'),
    path('login', views.login_view,name='login'),
    path('post', views.register,name='post'),#idk why is it working but dont touch it
    path('logout',views.logout_view, name='logout'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html') , name='reset_password'),

    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_sent.html') , name='password_reset_done'),

    path('reset_password/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_form.html') ,name='password_reset_confirm'),

    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html') , name='password_reset_complete'),

    path('myConferences', views.myConferences,name='myConferences'),
    path('about_myconf/<int:conf_id>/', views.about_myconf,name='about_myconf'),

    path('submitedArticles/<int:conf_id>/', views.submitedArticles,name='submitedArticles'),
]
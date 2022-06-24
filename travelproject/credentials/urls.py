from . import views
from django.urls import path

urlpatterns = [
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')

]
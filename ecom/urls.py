from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.login_view, name='login'),
    path('home/', views.index, name='home'),

    path('portfolio/<str:person>/', views.portfolio_view, name='portfolio'),
    path('portfolio/<str:person>/main/', views.portfolio_main_view, name='portfolio_main'),

    path('logout/', views.logout_view, name='logout'),
]
from django.contrib import admin
from django.urls import path
from blog.views import login_view, index, logout_view, portfolio_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('home/', index, name='home'),
    path('portfolio/<str:person>/', portfolio_view, name='portfolio'),
    path('logout/', logout_view, name='logout'),
]
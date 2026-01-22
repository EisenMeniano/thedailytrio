from django.contrib import admin
from django.urls import path
from blog.views import login_view, index, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),  # landing page is login
    path('home/', index, name='home'),   # user-specific home
    path('logout/', logout_view, name='logout'),
]
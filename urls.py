from django.contrib import admin
from django.urls import path
from apifoo.views import fetch_quotes, home

urlpatterns = [
    path('', home, name='home'),
    path("admin/", admin.site.urls),
    path('api/quotes/', fetch_quotes, name='fetch_quotes'),
]


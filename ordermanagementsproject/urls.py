from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin-page/', admin.site.urls),
    path("", include("ordermanagementsapp.urls"))
]
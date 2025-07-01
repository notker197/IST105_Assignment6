from django.contrib import admin
from django.urls import path
from bitwise.views import process_numbers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', process_numbers, name='home'),
]

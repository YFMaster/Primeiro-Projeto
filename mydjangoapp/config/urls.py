from django.contrib import admin
from django.urls import path
from apps.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.contest_list, name='contest_list'),
    path('export/', views.export_contests, name='contest_export'),
]

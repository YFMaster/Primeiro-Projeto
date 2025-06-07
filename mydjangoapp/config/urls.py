from django.contrib import admin
from django.urls import path
from apps.core import views
from apps.users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.contest_list, name='contest_list'),
    path('contest/<int:contest_id>/favorite/', user_views.add_favorite, name='add_favorite'),
    path('contest/<int:contest_id>/unfavorite/', user_views.remove_favorite, name='remove_favorite'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.new_show),
    path('shows/new/add', views.add_new_show),
    path('shows/<int:id>', views.display_show),
    path('shows/<int:id>/edit', views.edit_show),
    path('shows/<int:id>/edit/update', views.update),
    path('shows/<int:id>/delete', views.delete)
]
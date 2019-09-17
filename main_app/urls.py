from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path('add/', views.ItemCreate.as_view(), name="add_item"),
  path('<int:pk>/delete/', views.ItemDelete.as_view(), name="delete_item"),
]
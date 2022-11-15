from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.add, name='index'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('update/<int:task_id>/', views.update, name='update'),
    
]

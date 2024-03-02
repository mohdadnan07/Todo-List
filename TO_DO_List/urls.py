from django.urls import path,include
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.add_task, name='add_task'),
    path('complete_task/<int:id>/', views.complete_task, name="complete_task"),
    path('', views.abc, name='abc')
]

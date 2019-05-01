from django.urls import path
from . import views



urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('pst', views.post1_list, name='post1_list')
]

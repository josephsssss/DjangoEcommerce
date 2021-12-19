from django.urls import path, re_path, register_converter
from . import views

app_name = 'category'  # URL Reverse에서 namespace 역할

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    # path('new/', views.post_new, name='post_new'),
    #path('<int:pk>/', views.category_list, name='post_detail'),
]

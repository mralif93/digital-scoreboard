from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.Page1View, name='page_1_view'),
  path('v2/', views.Page2View, name='page_2_view'),
]
from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.LoadingView, name='page_loading_view'),
  path('v1/', views.Page1View, name='page_1_view'),
  path('v2/', views.Page2View, name='page_2_view'),
  path('v3/', views.Page3View, name='page_3_view'),
  path('v4/', views.Page4View, name='page_4_view'),
  path('v5/', views.Page5View, name='page_5_view'),
]
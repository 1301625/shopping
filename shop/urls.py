from django.urls import path, re_path
from . import views

app_name = 'shop'

urlpatterns = [
    path('',views.item_list, name='item_list'),
    path('<int:pk>/', views.item_detail, name='item_detail'),
    #re_path(r'^(?P<pk>\d+)/$', views.item_detail),


    path('new/', views.item_new, name='item_new'),
    path('<int:pk>/edit/', views.item_edit, name='item_edit'),
] 
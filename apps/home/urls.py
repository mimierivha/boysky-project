# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),  
    
     path('orders', views.order, name='orders'),

    path('orders-detail/<int:order_id>', views.landlord_detail, name='land-detail'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]


from django.contrib import admin
from django.urls import path, include
from core.views import ProductListCreate, ProductRetrieveUpdateDestroy

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('products/', ProductListCreate.as_view()),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view()),

]
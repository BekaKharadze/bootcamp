import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from core.models import Product

@pytest.mark.django_db
def test_product_list():
    client = APIClient()
    url = reverse('product-list')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_product():
    client = APIClient()
    url = reverse('product-list')
    data = {"name": "Laptop", "price": 999.99, "stock": 10}
    response = client.post(url, data, format='json')
    assert response.status_code == 201
    assert Product.objects.count() == 1
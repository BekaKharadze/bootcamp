from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from django.utils.cache import patch_vary_headers

@cache_page(60 * 15)
def slow_view(request):
    response = render(request, 'template_name', "erti ori")
    patch_vary_headers(response, ['Cookie'])
    return JsonResponse({"status": "Cached for 15 minutes"}), response

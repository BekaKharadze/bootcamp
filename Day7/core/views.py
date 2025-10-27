from django.shortcuts import render
from .tasks import send_welcome_email
from django.http import JsonResponse
new_user = 1234
def register_user(request):
    # create user
    send_welcome_email.delay(new_user.id)
    return JsonResponse({"status": "User created"})

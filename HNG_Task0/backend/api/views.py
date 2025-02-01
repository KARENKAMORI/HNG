from django.shortcuts import render
from django.http import JsonResponse
from django.utils.timezone import now

def public_api(request):
    response_data = {
        "email": "kamorikaren2019@gmail.com",
        "current_datetime": now().isoformat(),
        "github_url": "https://github.com/KARENKAMORI/HNG/tree/main/HNG_Task0/backend"
    }
    return JsonResponse(response_data)


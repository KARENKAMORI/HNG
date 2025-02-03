from django.shortcuts import render
from django.http import JsonResponse
from django.utils.timezone import now

def public_api(request):
    response_data = {
        "email": "kamorikaren2019@gmail.com",
        "current_datetime": now().replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "github_url": "https://github.com/KARENKAMORI/HNG"
    }
    return JsonResponse(response_data)


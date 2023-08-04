from django.shortcuts import render
from django.http import JsonResponse

async def get_marks(request):
    return JsonResponse({'ok' : 'hi'})

async def update_marks(requests):
    pass
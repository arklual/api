from django.views import View
from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from . import models
from api.settings import ALLOWED_TOKENS

@method_decorator(csrf_exempt, name='dispatch')
class Account(View):
    def get(self, request):
        headers = request.headers
        token = headers.get('Authorization').split(' ')[1] if headers.get('Authorization') and len(headers.get('Authorization').split(' ')) > 1 else ''
        if token not in ALLOWED_TOKENS: return HttpResponseForbidden('Forbidden')

        data = request.GET
        id = data.get('id')
        telegram_id = data.get('telegram_id')
        user = None
        if id:
            user = get_object_or_404(models.Account, id = id)
        elif telegram_id:
            user = get_object_or_404(models.Account, telegram_id=telegram_id)
        data = {
            'id': user.id,
            'telegram_id': user.telegram_id,
            'username': user.username,
            'is_admin': user.is_admin,
            'class': user.school_class
        }
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

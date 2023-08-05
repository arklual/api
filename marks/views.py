from django.views import View
from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from api.settings import ALLOWED_TOKENS
from . import models
from accounts.models import Account
from subjects.models import Subject
from asgiref.sync import sync_to_async

@method_decorator(csrf_exempt, name='dispatch')
class GetMarks(View):
    @sync_to_async
    def get_marks(self, user_id, subject_id):
        user = get_object_or_404(Account, id=user_id)
        subject = get_object_or_404(Subject, id=subject_id)
        marks = models.Marks.objects.filter(user=user, subject=subject)
        data = []
        for mark in marks:
            data.append({
                'subject_id': mark.subject.id,
                'subject_name': mark.subject.name,
                'value': mark.value,
                'id': mark.id
            })
        return data
    async def get_request(self, request):
        headers = request.headers
        token = headers.get('Authorization').split(' ')[1] if headers.get('Authorization') and len(headers.get('Authorization').split(' ')) > 1 else ''
        if token not in ALLOWED_TOKENS:
            return HttpResponseForbidden('Forbidden')
        data = request.GET
        user_id = data.get('user_id')
        subject_id = data.get('subject_id')
        data = await self.get_marks(user_id, subject_id)
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

async def update_marks(requests):
    pass
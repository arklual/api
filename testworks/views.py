from django.views import View
from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from . import models
from api.settings import ALLOWED_TOKENS
from accounts.models import Account
from subjects.models import Subject

@method_decorator(csrf_exempt, name='dispatch')
class AddWork(View):
    def post(self, request):
        headers = request.headers
        token = headers.get('Authorization').split(' ')[1] if headers.get('Authorization') and len(headers.get('Authorization').split(' ')) > 1 else ''
        if token not in ALLOWED_TOKENS: return HttpResponseForbidden('Forbidden')

        data = request.POST
        subject_id = data.get('subject_id')
        
        subject = get_object_or_404(Subject, id=subject_id)

        topic = data.get('topic')
        date = data.get('date')
        type = data.get('type')

        testwork = models.Testwork.objects.create(subject=subject, topic=topic, date=date, type=type)
        testwork.save()

        data = {
            'message': 'Testwork is created'
        }
        return JsonResponse(data, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class GetWorks(View):
    def get(self, request):
        headers = request.headers
        token = headers.get('Authorization').split(' ')[1] if headers.get('Authorization') and len(headers.get('Authorization').split(' ')) > 1 else ''
        if token not in ALLOWED_TOKENS: return HttpResponseForbidden('Forbidden')

        data = []

        tests = models.Testwork.objects.all()
        for test in tests:
            data.append({
                'subject_id': test.subject.id,
                'subject_name': test.subject.name,
                'topic': test.topic,
                'type': test.type,
                'date': test.date,
                'id': test.id,
            })
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

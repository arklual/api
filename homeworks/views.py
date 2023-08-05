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
class AddHomework(View):
    def post(self, request):
        headers = request.headers
        token = headers.get('Authorization').split(' ')[1] if headers.get('Authorization') and len(headers.get('Authorization').split(' ')) > 1 else ''
        if token not in ALLOWED_TOKENS: return HttpResponseForbidden('Forbidden')

        data = request.POST
        subject_id = data.get('subject_id')
        
        subject = get_object_or_404(Subject, id=subject_id)

        task = data.get('task')
        deadline = data.get('deadline')
        is_done = data.get('is_done')
        for user in Account.objects.all():
            hw = models.Homework.objects.create(subject=subject, user=user, task=task, deadline=deadline, is_done=is_done)
            hw.save()

        data = {
            'message': 'Homework is created'
        }
        return JsonResponse(data, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class GetHomeworks(View):
    def get(self, request):
        headers = request.headers
        token = headers.get('Authorization').split(' ')[1] if headers.get('Authorization') and len(headers.get('Authorization').split(' ')) > 1 else ''
        if token not in ALLOWED_TOKENS: return HttpResponseForbidden('Forbidden')

        data = request.GET
        user_id = data.get('user_id')
        user = get_object_or_404(Account, id=user_id)
        deadline = data.get('deadline')
        data = []
        hws = models.Homework.objects.filter(user = user, deadline=deadline)
        for hw in hws:
            data.append({
                'subject_id': hw.subject.id,
                'subject_name': hw.subject.name,
                'task': hw.task,
                'is_done': hw.is_done,
                'deadline': deadline,
                'id': hw.id,
            })
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

@method_decorator(csrf_exempt, name='dispatch')
class ChangeHomeworkDone(View):
    def get(self, request):
        headers = request.headers
        token = headers.get('Authorization').split(' ')[1] if headers.get('Authorization') and len(headers.get('Authorization').split(' ')) > 1 else ''
        if token not in ALLOWED_TOKENS: return HttpResponseForbidden('Forbidden')

        data = request.GET
        id = data.get('id')
        hw = get_object_or_404(models.Homework, id=id)
        hw.is_done = not hw.is_done
        hw.save()
        data = {
            'id': hw.id,
            'message': 'Homework is changed',
            'is_done': hw.is_done,
        }
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
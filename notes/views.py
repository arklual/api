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


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class AddNotes(View):
    def post(self, request):
        headers = request.headers
        token = headers.get('Authorization').split(' ')[1] if headers.get('Authorization') and len(headers.get('Authorization').split(' ')) > 1 else ''
        if token not in ALLOWED_TOKENS: return HttpResponseForbidden('Forbidden')

        data = request.POST
        subject_id = data.get('subject_id')
        
        subject = get_object_or_404(Subject, id=subject_id)

        task = data.get('author')
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
class GetNotes(View):
    def get(self, request):
        headers = request.headers
        token = headers.get('Authorization').split(' ')[1] if headers.get('Authorization') and len(headers.get('Authorization').split(' ')) > 1 else ''
        if token not in ALLOWED_TOKENS: return HttpResponseForbidden('Forbidden')

        data = request.GET
        subject_id = data.get('subject_id')
        subject = get_object_or_404(Subject, id=subject_id)
        data = []
        notes = models.Note.objects.filter(subject = subject)
        for note in notes:
            data.append({
                'author': note.author.first_name + ' ' + note.author.last_name,
                'subject_id': note.subject.id,
                'subject_name':note.subject.name,
                'date': note.date,
                'id': note.id,
            })
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
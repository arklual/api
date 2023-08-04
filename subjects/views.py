from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from api.settings import ALLOWED_TOKENS
from django.views import View
from django.http import JsonResponse, HttpResponseForbidden
from . import models

@method_decorator(csrf_exempt, name='dispatch')
class GetSubjects(View):
    def get(self, request):
        headers = request.headers
        token = headers.get('Authorization').split(' ')[1] if headers.get('Authorization') and len(headers.get('Authorization').split(' ')) > 1 else ''
        if token not in ALLOWED_TOKENS: return HttpResponseForbidden('Forbidden')

        data = request.GET
        data = []
        subjects = models.Subject.objects.all()
        for subject in subjects:
            data.append({
                'subject_id': subject.id,
                'subject_name': subject.name,
            })
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
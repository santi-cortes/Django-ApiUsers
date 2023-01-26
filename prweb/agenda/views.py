from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from agenda.models import create_list
from django.shortcuts import render
import json

class laprincipal(ListView):
    template_name = "agenda.html"
    model = create_list
    ordering = ['-id']
    
    


class agendaApi(View):
    def get(self, request):
        data = list(create_list.objects.values())
        return JsonResponse(data, safe=False)
    def post(self, request):
        data = json.loads(request.POST.get('datajson'))
        print(data)
        cnt = create_list(namel = data['nm'], userl = data['us'], datecl = data['dtc'], dateml = data['dtm'])
        cnt.save()
        return HttpResponse(json.dumps({'status': 'Se registro todo ok.'}), content_type='application/json')    


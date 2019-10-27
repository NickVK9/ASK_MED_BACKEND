from django.http import HttpResponse, HttpResponseRedirect
from .models import InsuranceCompany, Services
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
import json
from django.http import Http404

def index(request):
    latest_polis = InsuranceCompany.objects.filter(id=1)
    #output = latest_polis[0].polis_ltd_tel
    template = loader.get_template('service_check/index.html')
    context = {
        'id': latest_polis[0].polis_ltd_id,
    }
    return HttpResponse(template.render(context, request))

    #def detail(request, question_id):
        #question = get_object_or_404(Question, pk=question_id)
        #return render(request, 'polls/detail.html', {'question': question})

def results(request):
    all_services = {}
    output_services = []
    for q in Services.objects.all():
        all_services[q.polis_ltd_outservice] = q.polis_ltd_inclusion
    try:
        polis = InsuranceCompany.objects.get(polis_ltd_id=request.GET['polis_id'])
        list_of_services = request.GET['polis_outservice'].split(',')
        for service in list_of_services:
            service = service.strip()
            service = service.capitalize()
            if service in all_services:
                output_services.append(service + ' ' + all_services[service])
            else:
                output_services.append(service + ' ' + 'Услуга не найдена')
    except InsuranceCompany.DoesNotExist:
        return render(request, 'service_check/404.html')
    template = loader.get_template('service_check/result.html')
    context = {'type': polis.polis_ltd_type,
    'id': polis.polis_ltd_id,
    'date_end': polis.polis_ltd_date_end,
    'sk': polis.polis_ltd_sk,
    'tel': polis.polis_ltd_tel,
    'output': output_services}
    return HttpResponse(template.render(context, request))




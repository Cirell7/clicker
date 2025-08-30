from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from .models import Core

@csrf_exempt  # временно для упрощения
def index(request):
    core = Core.objects.first()

    if not core:
        core = Core.objects.create()
    

    if request.method == 'POST':
        core.click()
        return JsonResponse({
            'coins': core.coins,
            'click_power': core.click_power
        })

    return render(request, 'index.html', {'core': core})

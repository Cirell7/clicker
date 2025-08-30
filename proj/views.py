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
        action = request.POST.get('action')
        if action == 'click':
            core.click()
        elif action == 'save':
            core.save()
        return JsonResponse({
                'temporary_coins': core.get_temporary_coins(),
                'coins': core.get_coins(),
                'click_power': core.get_click_power(),
                'action': 'click'
            })

    return render(request, 'index.html', {'core': core})

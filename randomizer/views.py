from django.shortcuts import render
import random
from django.http import (JsonResponse, HttpResponse);


def random_secret(request):
    if request.method == 'GET': # and request.is_ajax()
        randomValue = random.random()
        return JsonResponse({'secret': randomValue})
        # return HttpResponse(randomValue)
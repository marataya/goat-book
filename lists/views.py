from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def home_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')

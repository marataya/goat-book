from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def home_page(request: HttpRequest) -> HttpResponse:
    new_item_text = request.POST.get('item_text', '')
    return render(request, 'home.html', {'new_item_text': new_item_text})

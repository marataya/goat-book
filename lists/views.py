from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from lists.models import Item


# Create your views here.
@csrf_exempt
def home_page(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        Item.objects.create(text=request.POST["item_text"])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {"items": items})

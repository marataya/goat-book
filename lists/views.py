from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from lists.models import Item


# Create your views here.
@csrf_exempt
def home_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')

@csrf_exempt
def view_list(request:HttpRequest):
    items = Item.objects.all()
    return (render(request, 'list.html', {"items": items}))

@csrf_exempt
def new_list(request:HttpRequest):
    Item.objects.create(text=request.POST["item_text"])
    return redirect('/lists/the-one-and-only-list/')

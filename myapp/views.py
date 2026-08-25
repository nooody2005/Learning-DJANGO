from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.

def index(request):
    # Getting items from database
    item_list = Item.objects.all()
    # Creating context
    context = {
        'item_list':item_list
    }
    # Passing the context object to the render method along with the template
    return render(request,"myapp/index.html",context)


    # return  HttpResponse(item_list)
    

def item(request):
    return HttpResponse("<h1>This is the item view</h1>")


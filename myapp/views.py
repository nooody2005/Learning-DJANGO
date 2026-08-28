from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
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
    

def detail(request,id):
    item = Item.objects.get(id=id)
    context = {
        'item' : item
    }
    return render(request,"myapp/detail.html",context)
    # return HttpResponse(f'This is the detail view for item {item}')

def item(request):
    return HttpResponse("<h1>This is the item view</h1>")

def create_item(request):
    form = ItemForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('myapp:index')
    context = {
        'form' : form
    }
    return render(request,'myapp/item-form.html',context)

def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance= item)
    if form.is_valid():
        form.save()
        return redirect('myapp:index')
    context = {
        'form' : form
    }
    return render(request,'myapp/item-form.html',context)


def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance= item)
    if form.is_valid():
        form.save()
        return redirect('myapp:index')
    context = {
        'form' : form
    }
    return render(request,'myapp/item-form.html',context)


def delete_item(request,id):
    item = Item.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return redirect('myapp:index')
    return render(request,'myapp/item-delete.html')


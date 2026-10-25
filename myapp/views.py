from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator 
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
import logging
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from .serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here.

logger = logging.getLogger(__name__)

# -------------------------------- API ------------------------------ 

# GET ALL THE ITEMS   & CREATE 
class ItemListAPIView(APIView):
    def get(self,request):
        # Get all items
        items = Item.objects.all()
        # converting data to json format
        serializer=ItemSerializer(items,many=True)
        return Response(serializer.data)
        
    def post(self,request):
        # Create new item
        serializer =  ItemSerializer(data=request.data)
        # Check if json data for new item valid or not 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 



# GET THE ITEM & UPDATE & DELETE 
class ItemDetailAPIView(APIView):
    # Check if the existed or not 
    def get_object(self,pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return None

    def get(self,request,pk):
        item = self.get_object(pk)
        if not item:
            return Response({"Error":"Item not Found (:"})
        
        # Get one item with its id
        serializer=ItemSerializer(item)
        return Response(serializer.data)

    def put(self,request,pk):
        item = self.get_object(pk)
        if not item:
            return Response({"Error":"Item not Found (:"})
        
        # Update the item 
        serializer=ItemSerializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self,request,pk):
        item = self.get_object(pk)
        if not item:
            return Response({"Error":"Item not Found (:"})

        # Delete the item 
        item.delete()
        return Response({"Item deleted successfully ^_^"})
        
        







# @api_view(["GET","POST"])
# def item_list_api(request):
#     if request.method == "GET":
#         # Get all items
#         items = Item.objects.all()
#         # converting data to json format
#         serializer=ItemSerializer(items,many=True)
#         return Response(serializer.data)
#     elif  request.method == "POST":
#         # Create new item
#         serializer =  ItemSerializer(data=request.data)
#         # Check if json data for new item valid or not 
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data) 




# @api_view(["GET","PUT","DELETE"])
# def item_detail_api(request,pk):

#     # Select the item
#     item = Item.objects.get(pk=pk)

#     if request.method == "GET":
#         # Get one item with its id
#         serializer=ItemSerializer(item)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         # Update the item 
#         serializer=ItemSerializer(item,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#     elif request.method == "DELETE":
#         # Delete the item 
#         item.delete()
#         return Response({"Item deleted successfully ^_^"})




# ---------------------------------------------------------------------

# def item_list_json(request):
#     items = Item.objects.all().values("id","item_name","item_desc","item_price")
#     return JsonResponse(list(items),safe=False)




# -----------------------------------------------------------------------------

# @login_required
# @cache_page(60 * 15)
# @vary_on_headers("User-Agent")
def index(request):
    # Getting items from database
    logger.info("Fetching all items from the database")
    logger.info(f"User [{timezone.now().isoformat()}] {request.user} requested item list from {request.META.get('REMOTE_ADDR')}")
    item_list = Item.objects.all()
    logger.debug(f"Found {item_list.count()} items")
    # print(item_list)
    paginator = Paginator(item_list,5)
    # print('paginator: ',paginator)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    # Creating context
    context = {
        'page_obj':page_obj
    }
    # Passing the context object to the render method along with the template
    return render(request,"myapp/index.html",context)


#     # return  HttpResponse(item_list)

# class IndexClassView(ListView):
#     model= Item
#     template_name = "myapp/index.html"
#     context_object_name = 'item_list'
    

def detail(request,id):
    logger.info("Fetching an item with id: {id}")
    try:
        item = get_object_or_404(Item,pk=id)
        # item = Item.objects.get(id=id)
        logger.debug(f"Item found {item.item_name} (${item.item_price})")
    except Exception as e:
        logger.error("Error fetching the item %s: %s",id ,e)
        raise

    context = {
        'item' : item
    }
    return render(request,"myapp/detail.html",context)
    # return HttpResponse(f'This is the detail view for item {item}')

# class FoodDetail(DetailView):
#     model = Item
#     template_name = 'myapp/detail.html'
#     context_object_name= 'item'
    

def item(request):
    return HttpResponse("<h1>This is the item view</h1>")

def create_item(request):
    form = ItemForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('myapp:index')

        else:
            print(form.errors)
            # print(form.errors['item_price'])
            
    context = {
        'form' : form
    }
    return render(request,'myapp/item-form.html',context)


# class ItemCreateView(CreateView): 
#     # item_form.html
#     # food --> food_form.html
#     model = Item
#     fields = ['item_name','item_desc','item_price','item_image']
#     def form_valid(self,form):
#         form.instance.user_name = self.request.user
#         return super().form_valid(form) 


# def update_item(request,id):
#     item = Item.objects.get(id=id)
#     form = ItemForm(request.POST or None, instance= item)
#     if form.is_valid():
#         form.save()
#         return redirect('myapp:index')
#     context = {
#         'form' : form
#     }
#     return render(request,'myapp/item-form.html',context)


class ItemUpdateView(UpdateView):
    model = Item
    fields =  ['item_name','item_desc','item_price','item_image']
    template_name_suffix = "_update_form"


def get_queryset(self):
    return Item.objects.filter(user_name = self.request.user)



# def delete_item(request,id):
#     item = Item.objects.get(id=id)
#     if request.method == "POST":
#         item.delete()
#         return redirect('myapp:index')
#     return render(request,'myapp/item-delete.html')



class ItemDelete(DeleteView):
    model= Item
    success_url = reverse_lazy("myapp:index")





def get_objects(request):
    for item in Item.objects.all():
        print(item.item_name)



def get_objects_optimized(request):
    items = Item.objects.only('item_name')
    for item in items:
        print(item.item_name)

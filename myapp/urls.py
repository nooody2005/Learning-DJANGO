from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


app_name='myapp'

urlpatterns = [
    # # URL Patterns of API
    # path('items-json/',views.item_list_json,name='item_list_json'),


    # =================================== URL patterns of API built with DRF ====================================
    # --------------- using Mixin --------------
    path('api/items',views.ItemListCreateAPI.as_view(),name='item-list-api'),
    # single item 
    path("api/items/<int:pk>",views.ItemRetrieveUpdateDestroyAPIView.as_view(),name='item-detail-api'),


    # ------------- using django view ----------
    # path('api/items',views.ItemListAPIView.as_view(),name='item-list-api'),
    # path("api/items/<int:pk>",views.ItemDetailAPIView.as_view(),name='item-detail-api'),


    # ------------- using old way --------------
    #  path('api/items',views.item_list_api,name='item-list-api'),
    # path("api/items/<int:pk>",views.item_detail_api,name='item-detail-api'),

    # ============================================ End of URL patterns of API =====================================


    # =========================================== URL Pattern of Django App =======================================

    # path('',views.IndexClassView.as_view(),name='index'),
    path('', views.index ,name='index'),
    # path('item/',views.item),
    path('<int:id>/',views.detail,name='detail'),
    # path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
     path('add/',views.create_item,name='create_item'),
    # path('add/',views.ItemCreateView.as_view(),name='create_item'),
    path('update/<int:pk>/',views.ItemUpdateView.as_view(),name='update_item'),
    path('delete/<int:pk>/',views.ItemDelete.as_view(),name='delete_item'),

    # ===========================================================================================================



]


from django.urls import path
from .views import (ProductAddView, RawMaterialAddView, 
                    PackingMaterialAddView, ManPowerAddView,EnergycostAddView,
                    ProductListView, RawMaterialListView,
                    PackingMaterialListView, ManPowerListView, EnergycostListView,
                    ProductUpdateView,RawMaterialUpdateView,
                    PackingMaterialUpdateView,ManPowerUpdateView, EnergycostUpdateView,
                    ProductDeleteView,RawMaterialDeleteView,
                    PackingMaterialDeleteView,ManPowerDeleteView, EnergycostDeleteView,
                    ProductDetailView,RawMaterialDetailView,
                    PackingMaterialDetailView,ManPowerDetailView, EnergycostDetailView,
                    SuperUserCreateView, LoginView, LogoutView)
                    
urlpatterns = [
    #Addview
    path('productadd/', ProductAddView.as_view(), name='product'),
    path('rawmaterialadd/', RawMaterialAddView.as_view(), name='rawmaterialadd'),
    path('packingmaterialadd/', PackingMaterialAddView.as_view(), name='packingmaterialadd'),
    path('manpoweradd/', ManPowerAddView.as_view(), name='manpoweradd'),
    path('energycostadd/', EnergycostAddView.as_view(), name='energyadd'),

    #Listview
    path('productlist/', ProductListView.as_view(), name='productlist'),
    path('rawmateriallist/', RawMaterialListView.as_view(), name='rawmateriallist'),
    path('packingmateriallist/', PackingMaterialListView.as_view(), name='packingmateriallist'),
    path('manpowerlist/', ManPowerListView.as_view(), name='manpowerlist'),
    path('energycostlist/', EnergycostListView.as_view(), name='energycostlist'),

    #Updateview
    path('productupdate/<str:product_name>/', ProductUpdateView.as_view(), name='productupdate'),
    path('rawmaterialupdate/<str:material_name>/', RawMaterialUpdateView.as_view(), name='rawmaterialupdate'),
    path('packingmaterialupdate/<str:pack_name>/', PackingMaterialUpdateView.as_view(), name='packingmaterialupdate'),
    path('manpowerupdate/<str:category_name>/', ManPowerUpdateView.as_view(), name='manpowerupdate'),
    path('energycostupdate/<str:category_name>/', EnergycostUpdateView.as_view(), name='energycostupdate'),


    #Deleteview
    path('productdelete/<str:product_name>/', ProductDeleteView.as_view(), name='productdelete'),
    path('rawmaterialdelete/<str:material_name>/', RawMaterialDeleteView.as_view(), name='rawmaterialdelete'),
    path('packingmaterialdelete/<str:pack_name>/', PackingMaterialDeleteView.as_view(), name='packingmaterialdelete'),
    path('manpowerdelete/<str:category_name>/', ManPowerDeleteView.as_view(), name='manpowerdelete'),
    path('energycostdelete/<str:category_name>/', EnergycostDeleteView.as_view(), name='energycostdelete'),

    #Detailview
    path('productdetail/<str:product_name>/', ProductDetailView.as_view(), name='productdetail'),
    path('rawmaterialdetail/<str:material_name>/', RawMaterialDetailView.as_view(), name='rawmaterialdetail'),
    path('packingmaterialdetail/<str:pack_name>/', PackingMaterialDetailView.as_view(), name='packingmaterialdetail'),
    path('manpowerdetail/<str:category_name>/', ManPowerDetailView.as_view(), name='manpowerdetail'),
    path('energycostdetail/<str:category_name>/', EnergycostDetailView.as_view(), name='energycostdetail'),

    path('create/', SuperUserCreateView.as_view(), name='superuser-create'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name='logout')
]

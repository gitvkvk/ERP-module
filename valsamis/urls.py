from django.urls import path
from . import views
from .views import *







urlpatterns = [
       path('', views.index, name='index'),
       path('databases', views.databases, name='databases'),
       path('forms', views.formspage, name='forms'),
       path('companyform', views.companyformview, name = 'companyform'),
       
       path('databases/branchview', views.branchview, name='branchview'),
       path('databases/projectview', views.projectview, name='projectview'),
       path('databases/customerview', views.customerview, name='customerview'),
       path('databases/purchaseorders', views.POListView.as_view(), name='POListView'),
       path('databases/purchaseorders/<int:pk>', views.PODetailView.as_view(), name='purchase-order-detail'),

       path('PurchaseOrderAddURL', views.PurchaseOrderAddView, name='PurchaseOrderAdd'),

       
       
       
       
     
]

"""should be named purchaseorderaddPath"""
"""needs a pk?

old path PurchaseOrderAddURL/<int:pk>
"""  
      



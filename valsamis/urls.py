from django.urls import path
from . import views
from .views import *







urlpatterns = [
       path('', views.index, name='index'), #home
       path('databases', views.databases, name='databases'),
       path('forms', views.formspage, name='forms'),


       
       path('databases/branchview', views.branchview, name='branchview'),
       path('databases/projectview', views.projectview, name='projectview'),
       path('databases/customerview', views.customerview, name='customerview'),


       path('databases/purchaseorders', views.POListView.as_view(), name='POListView'), #list view
       path('databases/purchaseorders/<int:pk>', views.PODetailView.as_view(), name='purchase-order-detail'), #detail view



       path('shiplist', views.shiplist, name='shiplist'),
       path('shipform', views.shipformview, name='shipformURL'),  # get and post request for insert operation
       path('shipform/<int:id>/', views.shipformview, name='shipupdateURL'), # get and post request for update operation
       path('shipdelete/<int:id>/', views.shipdelete, name='shipdeleteURL'), #get request to retrieve and display all records

  

       
       
       
       
     
]

"""should be named purchaseorderaddPath"""
"""needs a pk?

old path PurchaseOrderAddURL/<int:pk>
"""  
      



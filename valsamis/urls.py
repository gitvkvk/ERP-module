from django.urls import path, re_path
from . import views
from .views import *

from django_filters.views import FilterView
from valsamis.filters import UserFilter


urlpatterns = [

       path('bootstrap', views.BootstrapFilterView, name = 'bootstrap'),

       #Base URLs
       path('', views.index, name='index'), #home
       path('databases', views.databases, name='databases'),
       path('forms', views.formspage, name='forms'),
       #purpose is to show number of ships in database, can delete these later
       path('databases/branchview', views.branchview, name='branchview'),
       path('databases/customerview', views.customerview, name='customerview'),

#ships
       #list 
       path('shiplist', views.shiplist, name='shiplist'), #targeting this to make it filter-form

       #CRUD
       path('shipform', views.shipformview, name='shipformURL'),  # get and post request for insert operation
       path('shipform/<int:id>/', views.shipformview, name='shipupdateURL'), # get and post request for update operation
       path('shipdelete/<int:id>/', views.shipdelete, name='shipdeleteURL'), #get request to retrieve and display all records

#PO 
       #list and detail
       path('POfilterlistview', views.POFilterListView, name = 'POfilterlistviewURL'),
              #path('databases/purchaseorders', views.POListView.as_view(), name='POListView'), 
       path('databases/purchaseorders/<int:pk>', views.MaterialItemRegisterView, name='purchase-order-detail'), #detail view
                     #changed view from (views.PODetailView.as_view()) into new none generic view
       path('databases/itemregister/', views.MaterialItemRegisterView, name='itemregisterURL'),

       #can follow ship form above, if pk = 0 take to a different html that has filter
       #now, if you have purchaseorders/0 it works, but purchaseorder/ does not
       

       #CRUD
       path('POform', views.POformview, name='POformURL'),  # get and post request for insert operation
       path('POform/<int:id>/', views.POformview, name='POupdateURL'), # get and post request for update operation
       path('POdelete/<int:id>/', views.POdelete, name='POdeleteURL'), #get request to retrieve and display all records

       #generate PDF
       path('POpdf', views.POpdfview, name='POpdfURL'), 


#filters

       #filter-form URL

      # re_path(r'^search/$', views.search, name ='search')

       re_path(r'^search/$', FilterView.as_view(filterset_class=UserFilter, template_name='valsamis/user_list.html'), name ='search'),







  

       
       
       
       
     
]

"""should be named purchaseorderaddPath"""
"""needs a pk?

old path PurchaseOrderAddURL/<int:pk>
"""  
      



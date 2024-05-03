
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/vendors/', views.vendors_list), #handles GET and POST
    path('api/vendors/<int:vendor_code>', views.vendors_detail), # handles 'GET','PUT','DELETE' request
    
    path('api/purchase_orders/', views.purchase_orders_list), #handles GET and POST
    path('api/purchase_orders/<int:po_number>', views.purchase_orders), # handles 'GET','PUT','DELETE' request
    
    #path('fruits/<int:id>',views.fruit_detail)
    
]

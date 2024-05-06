
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("api/vendors/", views.VendorListCreateView.as_view(), name="vendors_list"),
    path("api/vendors/<int:pk>/",views.VendorRetrieveUpdateDestroyView.as_view(),
         name="vendor_detail"),
    path("api/vendors/<int:pk>/performance/",views.VendorPerformanceView.as_view(),
         name="vendor_performance",),
    
    path('api/purchase_orders/', views.PurchaseOrderListCreateView.as_view(), 
        name="purchase_order_list"), #handles GET and POST
    path('api/purchase_orders/<int:pk>/', views.PurchaseOrderRetrieveUpdateDestroyView.as_view(),
        name="purchase_order_detail",), #handle 'GET','PUT','DELETE'
    path("api/purchase_orders/<int:pk>/acknowledge/",
        views.PurchaseOrderAcknowledgeView.as_view(),
        name="purchase_order_acknowledge",
        ),
    
]

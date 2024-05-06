from django.shortcuts import render
from  .serializer import ( VendorSerializer,
                          VendorPerformanceSerializer,
                          PurchaseOrderSerializer,
                          PurchaseOrderAcknowledgeSerializer
                        )
from rest_framework.decorators import api_view
from  rest_framework.response import Response
from  rest_framework import status
from  .models import Vendor , PurchaseOrder

# Create your views here.
from rest_framework import generics

class VendorListCreateView(generics.ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
class VendorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorPerformanceView(generics.RetrieveAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceSerializer

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

#NOTE: To acknowledge a purchase order, the vendor has to enter an 
# 'acknowledgement_date' field. Since this field is getting updated,
# so I am using PUT and not POST as required in original assignment. 
#I hope this is fine.
class PurchaseOrderAcknowledgeView(generics.UpdateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderAcknowledgeSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid()
        self.perform_update(serializer=serializer)
        return Response(
            {
                "status": "success",
                "message": "CONGRATS: Purchase order successfully acknowledged.",
                "code": "success_acknowledgement",
            },
            status=status.HTTP_200_OK,
        )



"""
@api_view(['GET','POST'])
def vendors_list(request, format=None):
    
    if request.method == 'GET':
        vendor = Vendor.objects.all() #get all vendors
        serializer = VendorSerializer(vendor, many=True)
        return Response(serializer.data) 
    
    if request.method == 'POST': #create a new vendor
        serializer = VendorSerializer(data = request.data)
        #print("serializer=",serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#end def

@api_view(['GET','PUT','DELETE'])
def vendors_detail(request,vendor_id, format=None):
    try:
        vendor = Vendor.objects.get(id=vendor_id)
    except Vendor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
  
    if request.method == 'GET': # process GET request from 127.0.0.1:8000/vendor/{vendor_code}
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)
    
    elif request.method == 'PUT': # process PUT request from 127.0.0.1:8000/vendor/{vendor_code}
        serializer = VendorSerializer(vendor, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    #end def

    elif request.method == 'DELETE': # process DELETE request from 127.0.0.1:8000/vendor/{vendor_code}
        vendor.delete()
        return Response({'deleted':'successfully deleted ' + str(vendor)}) 
    #end def

    else:
        return Response( {'Invalid request method':str(request.method)} ) 
#end def    



@api_view(['GET','POST'])
def purchase_orders_list(request, format=None):
    
    if request.method == 'GET':
        vendor = PurchaseOrder.objects.all() #get all po
        serializer = PurchaseOrderSerializer(vendor, many=True)
        return Response(serializer.data) 
    
    elif request.method == 'POST': #create a new po
        #print("in POST")
        serializer = PurchaseOrderSerializer(data = request.data)
        #print("serializer=",serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    else:
        return Response( {'Invalid request method':str(request.method)} ) 
    
#end def

@api_view(['GET','PUT','DELETE'])
def purchase_orders(request, po_id , format=None):
    try:
        po = PurchaseOrder.objects.get(id=po_id)
    except PurchaseOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
  
    if request.method == 'GET': # process GET request from 127.0.0.1:8000/purchase_orders/{po_id}
        serializer = PurchaseOrderSerializer(po)
        return Response(serializer.data)
    
    elif request.method == 'PUT': # process PUT request from 127.0.0.1:8000/purchase_orders/{vendor_code}
        serializer = PurchaseOrderSerializer(po, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    #end def

    elif request.method == 'DELETE': # process DELETE request from 127.0.0.1:8000/purchase_orders/{vendor_code}
        po_str =  str(po)
        po.delete()
        return Response({'deleted':'Successfully deleted ' + po_str  }) 
    #end def

    else:
        return Response( {'Invalid request method':str(request.method)} ) 
#end def    
"""





from django.shortcuts import render
from  .serializer import VendorSerializer, PurchaseOrderSerializer
from rest_framework.decorators import api_view
from  rest_framework.response import Response
from  rest_framework import status
from  .models import Vendor , PurchaseOrder

# Create your views here.
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
def vendors_detail(request,vendor_code, format=None):
    try:
        vendor = Vendor.objects.get(vendor_code=vendor_code)
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
        serializer = PurchaseOrderSerializer(data = request.data)
        print("serializer=",serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    else:
        return Response( {'Invalid request method':str(request.method)} ) 
    
#end def

@api_view(['GET','PUT','DELETE'])
def purchase_orders(request, po_number , format=None):
    try:
        po = PurchaseOrder.objects.get(po_number=po_number)
    except PurchaseOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
  
    if request.method == 'GET': # process GET request from 127.0.0.1:8000/vendor/{vendor_code}
        serializer = PurchaseOrderSerializer(po)
        return Response(serializer.data)
    
    elif request.method == 'PUT': # process PUT request from 127.0.0.1:8000/vendor/{vendor_code}
        serializer = PurchaseOrderSerializer(po, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    #end def

    elif request.method == 'DELETE': # process DELETE request from 127.0.0.1:8000/vendor/{vendor_code}
        po.delete()
        return Response({'deleted':'successfully deleted ' + str(po)}) 
    #end def

    else:
        return Response( {'Invalid request method':str(request.method)} ) 
#end def    


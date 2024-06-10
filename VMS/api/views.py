from django.shortcuts import render
from  .serializer import ( VendorSerializer,
                          VendorPerformanceSerializer,
                          PurchaseOrderSerializer,
                          PurchaseOrderAcknowledgeSerializer
                        )
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from  .models import Vendor , PurchaseOrder
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
#from rest_framework_simplejwt.authentication import JWTAuthentication #I experimented with this and it is NOT NEEDED

# Create your views here.
class VendorListCreateView(generics.ListCreateAPIView):
    #authentication_classes = [JWTAuthentication]# Authentication identifies the user
    permission_classes = (IsAuthenticated,)# Allows only authenticated users to access this view
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
class VendorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorPerformanceView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceSerializer

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

#NOTE: To acknowledge a purchase order, the vendor has to enter an 
# 'acknowledgement_date' field. Since this field is getting updated,
# so I am using PUT and not POST as required in original assignment. 
#I hope this is fine.
class PurchaseOrderAcknowledgeView(generics.UpdateAPIView): #Gets called on PUT or PATCH(i.e. partial data is passed)
    #permission_classes = (IsAuthenticated,)
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderAcknowledgeSerializer
    
    #override
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer=serializer) #This invokes update method of serializer
            return Response(
                {
                    "status": "success",
                    "message": "CONGRATS: Purchase order successfully acknowledged.",
                    "code": "success_acknowledgement",
                },
                status=status.HTTP_200_OK,
            )

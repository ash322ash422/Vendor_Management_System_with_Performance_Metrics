from rest_framework import serializers
from  .models import (Vendor,
                      PurchaseOrder,
                      OrderStatus
                      )
from .my_signals import ( po_acknowledged_signal,
                          po_status_completed_signal,
                        )
 
class VendorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vendor
        fields = '__all__'
        read_only_fields = ["id","created_at","updated_at"]
    #end class
#end class

class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = [
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]
#end class

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if instance.status == OrderStatus.COMPLETED:
            po_status_completed_signal.send(
                sender=instance.__class__, instance=instance
            )
        return instance




class PurchaseOrderAcknowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ["acknowledgment_date"]
        extra_kwargs = {"acknowledgment_date": {"required": True}}

    def validate_acknowledgment_date(self, value):
        if not value:
            value = timezone.now()
        return value

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        po_acknowledged_signal.send(sender=instance.__class__,
                                    instance=instance )
        
        return instance

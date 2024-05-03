from django.db import models
from django.utils import timezone

CHOICES_STATUS= (('pending','Pending'),
                 ('completed','Completed'),
                 ('cancelled','Cancelled')
                 )

# Create your models here.
class Vendor(models.Model):
    name =  models.CharField(max_length=50, blank=True, null=True,unique=True) # Vendor's name.
    contact_details = models.TextField(help_text="Contact information of the vendor") # Contact information of the vendor.
    address = models.TextField(help_text="Physical address of the vendor") #Physical address of the vendor.
    vendor_code = models.CharField(unique=True, max_length=10) # A unique identifier for the vendor.
    on_time_delivery_rate = models.FloatField(help_text="Tracks the percentage of on-time deliveries") # Tracks the percentage of on-time deliveries.
    quality_rating_avg = models.FloatField(help_text="Average rating of quality based on purchase orders") # Average rating of quality based on purchase orders.
    average_response_time = models.FloatField(help_text="Average time taken to acknowledge purchase orders") # Average time taken to acknowledge purchase orders.
    fulfillment_rate = models.FloatField(help_text="Percentage of purchase orders fulfilled successfully") # Percentage of purchase orders fulfilled successfully
    
    def __str__(self):
        return '{} - {}'.format(self.name ,self.vendor_code)
#end class

class PurchaseOrder(models.Model):
    po_number = models.CharField(unique=True, max_length=10) # Unique number identifying the PO.
    vendor = models.ForeignKey(to=Vendor,to_field='name', on_delete=models.CASCADE) # Link to the Vendor model.
    # order_date = models.DateTimeField(auto_now_add=True) # Date when the order was placed.
    # delivery_date = models.DateTimeField(blank=True) # Expected or actual delivery date of the order.
    # items = models.JSONField(null=False,default='') # Details of items ordered.
    # quantity = models.IntegerField(default=1) # Total quantity of items in the PO.
    # status = models.CharField(choices=CHOICES_STATUS, blank=False, max_length=10,default=CHOICES_STATUS[0]) # Current status of the PO (e.g., pending, completed, canceled).
    # quality_rating = models.FloatField(null=True,blank=True) # Rating given to the vendor for this PO (nullable).
    # issue_date = models.DateTimeField(blank=False, default = timezone.now ) # Timestamp when the PO was issued to the vendor.
    # acknowledgment_date = models.DateTimeField(blank=True, null=True) #, nullable - Timestamp when the vendor acknowledged the PO

#end class
    
class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(to=Vendor, on_delete=models.CASCADE) # - Link to the Vendor model.
    date = models.DateTimeField(blank=False) # Date of the performance record.
    on_time_delivery_rate = models.FloatField() # Historical record of the on-time delivery rate.
    quality_rating_avg = models.FloatField() # Historical record of the quality rating average.
    average_response_time = models.FloatField() # Historical record of the average response time.
    fulfillment_rate = models.FloatField() # Historical record of the fulfillment rate
#end class




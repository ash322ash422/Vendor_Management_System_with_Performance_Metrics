from rest_framework import serializers
from  .models import Vendor, PurchaseOrder

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['po_number','vendor']
        
        po_number = serializers.CharField()
        vendor = 'v22'
"""
    

order_date = models
delivery_date = mod
items = models.JSON
quantity = models.I
status = models.Cha
quality_rating = mo
issue_date = models
acknowledgment_date
#end class

"""

class VendorSerializer(serializers.ModelSerializer):
    p_orders = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Vendor
        fields = '__all__' # This would retrieve all fields
        #exclude = ['average_response_time']
    #end class
#end class


"""
class SongSerializer(serializers.ModelSerializer):
    class Meta:
      model = Song
      fields = ('id', 'name')
      
class ArtistSerializer(serializers.ModelSerializer):
  songs = SongSerializer(many=True)
   
  class Meta:
    model = Artist
    fields = ('id', 'name', 'songs')
"""    

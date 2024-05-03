from .models import Vendor, PurchaseOrder, HistoricalPerformance
from django.forms import ModelForm, Textarea

class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = ["name","contact_details","address", "vendor_code","on_time_delivery_rate",
               "quality_rating_avg", "average_response_time",
               ] 

        #  widgets = { #TODO
        #       'contact_details': Textarea(attrs={'rows':4, 'cols':15}),
        #         'address':  Textarea(attrs={'rows':4, 'cols':15}),
        #     
        #   }

#end class

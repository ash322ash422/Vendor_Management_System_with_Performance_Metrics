import requests
import json
from django.utils import timezone


#Send a GET request to retrieve all purchase_orders
print("Sending GET /api/purchase_orders/")
response = requests.get('http://127.0.0.1:8000/api/purchase_orders/')
print('Response from server: ' + str(response.json()))

#Send a POST request to create a new po
print("Sending POST /api/purchase_orders/")
response = requests.post("http://127.0.0.1:8000/api/purchase_orders/", 
    data={'po_number': '3', 
          'order_date': timezone.now,
          'delivery_date': timezone.now,
          'items': 'Box', 
          'quantity': 1,
          'status': 'pending',
          'quality_rating': 1.0,
          'issue_date': timezone.now,
          'acknowledgment_date': timezone.now,
          'vendor': 39
          },
    #headers={"Content-Type": "application/json"},
)
print('Response from server: ' + str(response.json()))
print("########################################")

"""
print("#################################################")
#Send a POST request to create a new purchase_orders
print("Sending POST /api/purchase_orders/")
response = requests.post("http://127.0.0.1:8000/api/purchase_orders/", 
    data={'name': 'vendor3', 'contact_details': 'vendor3 contact details here',
          'address': 'vendor3 address here', 'vendor_code': '3', 
          'on_time_delivery_rate': 1.0, 'quality_rating_avg': 1.0, 'fulfillment_rate': 1.0,
          'average_response_time': 3.0
          },
    #headers={"Content-Type": "application/json"},
)
print('Response from server: ' + str(response.json()))


print("#################################################")
#Send a GET request to retrieve data on vendor with vendor_code=3
print("Sending GET /api/vendors/3")
response = requests.get("http://127.0.0.1:8000/api/vendors/3", )
print('Response from server: ' + str(response.json()))

print("#################################################")
#Send a PUT request to update vendor with vendor_code=2
print("Sending PUT /api/vendors/2")
response = requests.put("http://127.0.0.1:8000/api/vendors/2", 
    data={'name': 'vendor2 updated', 'contact_details': 'vendor2 updated contact details here',
          'address': 'vendor2 updated address here', 'vendor_code': '2', 
          'on_time_delivery_rate': 4.0, 'quality_rating_avg':21.0, 'fulfillment_rate': 3.0,
          'average_response_time': 4.0
          },
    #headers={"Content-Type": "application/json"},
)
print('Response from server: ' + str(response.json()))

print("#################################################")
print("Sending DELETE /api/vendors/3")
response = requests.delete( "http://127.0.0.1:8000/api/vendors/3",
                            data=json.dumps({'vendor_code': 3})
                          )
print('Response from server: ' + str(response.json()))


"""
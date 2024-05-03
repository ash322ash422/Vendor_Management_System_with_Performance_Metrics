import requests
import json

#Send a POST request to create a new vendor
print("Sending POST /api/vendors/")
response = requests.post("http://127.0.0.1:8000/api/vendors/", 
    data={'name': 'vendor1', 'contact_details': 'vendor1 contact details here',
          'address': 'vendor1 address here', 'vendor_code': '1', 
          'on_time_delivery_rate': 1.0, 'quality_rating_avg': 1.0, 'fulfillment_rate': 1.0,
          'average_response_time': 1.0
          },
    #headers={"Content-Type": "application/json"},
)
print('Response from server: ' + str(response.json()))

print("Sending POST /api/vendors/")
response = requests.post("http://127.0.0.1:8000/api/vendors/", 
    data={'name': 'vendor2', 'contact_details': 'vendor2 contact details here',
          'address': 'vendor2 address here', 'vendor_code': '2', 
          'on_time_delivery_rate': 2.0, 'quality_rating_avg': 2.0, 'fulfillment_rate': 2.0,
          'average_response_time': 2.0
          },
    #headers={"Content-Type": "application/json"},
)
print('Response from server: ' + str(response.json()))
print("########################################")

#Send a GET request to retrieve all vendors
print("Sending GET /api/vendors/")
response = requests.get('http://127.0.0.1:8000/api/vendors/')
print('Response from server: ' + str(response.json()))

print("#################################################")
#Send a POST request to create a new vendor
print("Sending POST /api/vendors/")
response = requests.post("http://127.0.0.1:8000/api/vendors/", 
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

print("#################################################")
print("Now we delete all vendors that we created in this test script:")
print("Sending DELETE /api/vendors/1")
response = requests.delete( "http://127.0.0.1:8000/api/vendors/1",
                            data=json.dumps({'vendor_code': '1'})
                          )
print("Sending DELETE /api/vendors/2")
print('Response from server: ' + str(response.json()))

response = requests.delete( "http://127.0.0.1:8000/api/vendors/2",
                            data=json.dumps({'vendor_code': '2'})
                          )
print('Response from server: ' + str(response.json()))


import requests
import json
import os

vendor_code_for_test = ['1','2','3']
#Send a POST request to create a new vendor
print("****************Running ",os.path.basename(__file__),"**************************")
print("Creating 3 vendors for testing.....")
print("Sending POST /api/vendors/")
response = requests.post("http://127.0.0.1:8000/api/vendors/", 
    data={'name': 'vendor1', 'contact_details': 'vendor1 contact details here',
          'address': 'vendor1 address here',
          'vendor_code': vendor_code_for_test[0], 
          'on_time_delivery_rate': 1.0, 'quality_rating_avg': 1.0, 'fulfillment_rate': 1.0,
          'average_response_time': 1.0
          },
    #headers={"Content-Type": "application/json"},
)
print('Response from server: ' + str(response.json()))

print("Sending POST /api/vendors/")
response = requests.post("http://127.0.0.1:8000/api/vendors/", 
    data={'name': 'vendor2', 'contact_details': 'vendor2 contact details here',
          'address': 'vendor2 address here',
          'vendor_code': vendor_code_for_test[1], 
          'on_time_delivery_rate': 2.0, 'quality_rating_avg': 2.0, 'fulfillment_rate': 2.0,
          'average_response_time': 2.0
          },
    #headers={"Content-Type": "application/json"},
)
print('Response from server: ' + str(response.json()))
print("Sending POST /api/vendors/")
response = requests.post("http://127.0.0.1:8000/api/vendors/", 
    data={'name': 'vendor3', 'contact_details': 'vendor3 contact details here',
          'address': 'vendor3 address here',
          'vendor_code': vendor_code_for_test[2], 
          'on_time_delivery_rate': 3.0, 'quality_rating_avg': 3.0, 'fulfillment_rate': 3.0,
          'average_response_time': 3.0
          },
    #headers={"Content-Type": "application/json"},
)
print('Response from server: ' + str(response.json()))

print("########################################")


#Send a GET request to retrieve all vendors
print("Sending GET /api/vendors/")
response = requests.get('http://127.0.0.1:8000/api/vendors/')
print('Response from server: ' + str(response.json()))
response_list_of_dict = json.loads(response.text)
print("Number of vendor:", len(response_list_of_dict))
for i in range(len(response_list_of_dict)):
    print("..vendor num {} = {}".format(i,response_list_of_dict[i]))


print("#################################################")
#Send a POST request to create a new vendor
vendor_code_test = '33'
print("Sending POST /api/vendors/")
response = requests.post("http://127.0.0.1:8000/api/vendors/", 
    data={'name': 'vendor3', 'contact_details': 'vendor3 contact details here',
          'address': 'vendor3 address here', 'vendor_code': vendor_code_test, 
          'on_time_delivery_rate': 1.0, 'quality_rating_avg': 1.0, 'fulfillment_rate': 1.0,
          'average_response_time': 3.0
          },
    #headers={"Content-Type": "application/json"},
)
print('Response from server: ' + str(response.json()))

response_dict = json.loads(response.text)
vendor_id_created = response_dict["id"]
print("vendor_id_created ={}".format(response_dict["id"])) 
#Now we delete this vendor we just created
print("Sending DELETE /api/vendors/{}/".format(vendor_id_created))
response = requests.delete( "http://127.0.0.1:8000/api/vendors/{}".format(vendor_id_created),)
#print('Response from server: ' + str(response.json()))
print("Successfully deleted vendor_id = {}".format(vendor_id_created))

print("#################################################")
#Send a GET request to retrieve data on specific vendor 
response = requests.get('http://127.0.0.1:8000/api/vendors/')#get list of vendors
response_list_of_dict = json.loads(response.text)
vendor_id = response_list_of_dict[0]["id"] #pick 1st vendor

print("Sending GET /api/vendors/{}/".format(vendor_id))
response = requests.get("http://127.0.0.1:8000/api/vendors/{}/".format(vendor_id), )
print('Response from server: ' + str(response.json()))

print("#################################################")
#Send a PUT request to update this vendor
print("Sending PUT /api/vendors/{}/".format(vendor_id))
response = requests.put("http://127.0.0.1:8000/api/vendors/{}/".format(vendor_id), 
    data={'name': response_list_of_dict[0]["name"], 
          'contact_details': response_list_of_dict[0]["contact_details"],
          'address': response_list_of_dict[0]["address"],
          'vendor_code': response_list_of_dict[0]["vendor_code"], 
          'on_time_delivery_rate': 4.0,
          'quality_rating_avg':21.0, 
          'fulfillment_rate': 3.0,
          'average_response_time': 4.0
          },
    #headers={"Content-Type": "application/json"},
)
print('Response from server: ' + str(response.json()))

print("#################################################")
print("Now we delete all vendors that we created in this test script:")
 #we delete all these vendors
for i in range(len(response_list_of_dict)):
    if response_list_of_dict[i]["vendor_code"] in vendor_code_for_test:
       vendor_id = response_list_of_dict[i]["id"]
       print("Sending DELETE /api/vendors/{}/".format(vendor_id))
       response = requests.delete( "http://127.0.0.1:8000/api/vendors/{}/".format(vendor_id),)
       print("..Successfully deleted vendor_id = {}".format(vendor_id))

print("Successfully deleted all vendors that we created in this test script.")
print();print();print();print();print();

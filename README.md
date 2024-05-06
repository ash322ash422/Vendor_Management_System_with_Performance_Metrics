# Vendor_Management_System_with_Performance_Metrics
 
 I used python3.11 for this project.
*) Get a clone of the project:
git clone https://github.com/ash322ash422/Vendor_Management_System_with_Performance_Metrics Vendor_Management_System_with_Performance_Metrics

and then go into the project directory:

 'cd Vendor_Management_System_with_Performance_Metrics'

*) Create a virtual env:
FOR WINDOWS: First run 'python -m venv venv' and then run 'venv\Scripts\activate'

*) Install all required packages:
...\Vendor_Management_System_with_Performance_Metrics> pip install -r requirements.txt

*) Go into VMS directory, and enter following commands:
...\Vendor_Management_System_with_Performance_Metrics\VMS> python manage.py makemigrations

*)
...\Vendor_Management_System_with_Performance_Metrics\VMS> python manage.py migrate 

*)
...\Vendor_Management_System_with_Performance_Metrics\VMS> python manage.py createsuperuser

*)
...\Vendor_Management_System_with_Performance_Metrics\VMS> python manage.py runserver

Now if you goto URL 'http://127.0.0.1:8000', you would see all endpoints.

*) Perform individual test by opening another terminal and type following command to test (inside indicated directory):
NOTE: Make sure you are in virtual env. created above.

...\Vendor_Management_System_with_Performance_Metrics\VMS\api> python test_api1_vendors.py

This checks following endpoints:
POST /api/vendors/
GET /api/vendors/
GET /api/vendors/{vendor_id}/
PUT /api/vendors/{vendor_id}/
DELETE /api/vendors/{vendor_id}/


...\Vendor_Management_System_with_Performance_Metrics\VMS\api> python test_api2_purchase_orders.py

This checks following endpoints:
POST /api/purchase_orders/
GET /api/purchase_orders/
GET /api/purchase_orders/{po_id}/
PUT /api/purchase_orders/{po_id}/
DELETE /api/purchase_orders/{po_id}/

...\Vendor_Management_System_with_Performance_Metrics\VMS\api> python test_api3_backend_logic.py

This checks following endpoints:
GET /api/vendors/{vendor_id}/performance/
GET /api/vendors/{vendor_id}/performance/
PUT /api/purchase_orders/{po_id}/acknowledge/

-OR- you can run all of the above 3 test by going up 1 directory and simply typing:

...\Vendor_Management_System_with_Performance_Metrics\VMS> python manage.py test

*) I performed above test and output is given in file test_output.txt
# Vendor_Management_System_with_Performance_Metrics
 
 I used python3.11 for this project.

*) Get a clone of the project:

git clone https://github.com/ash322ash422/Vendor_Management_System_with_Performance_Metrics my_project

and then go into the project directory:

 'cd my_project'

*) Create a virtual env. using python3.11 as shown in steps below:

FOR WINDOWS: First run 'python -m venv venv' and then run 'venv\Scripts\activate'

*********************************

EXAMPLE OF ABOVE PROCEDURE ON MY COMPUTER:

C:\Users\hi> git clone https://github.com/ash322ash422/Vendor_Management_System_with_Performance_Metrics my_project

Cloning into 'my_project'...

remote: Enumerating objects: 107, done.

remote: Counting objects: 100% (107/107), done.

remote: Compressing objects: 100% (75/75), done.

remote: Total 107 (delta 41), reused 93 (delta 27), pack-reused 0

Receiving objects: 100% (107/107), 74.71 KiB | 513.00 KiB/s, done.

Resolving deltas: 100% (41/41), done.

C:\Users\hi> cd my_project

C:\Users\hi\my_project> C:\Users\hi\AppData\Local\Programs\Python\Python311\python.exe -m venv venv   <-NOTE: I am using python3.11

C:\Users\hi\my_project> venv\Scripts\activate

(venv) C:\Users\hi\my_project>

*********************************

*) Install all required packages:

(venv) C:\Users\hi\my_project> pip install -r requirements.txt

*) Go into VMS directory, and enter migrations commands:

(venv) C:\Users\hi\my_project> cd VMS

(venv) C:\Users\hi\my_project\VMS> python manage.py makemigrations

(venv) C:\Users\hi\my_project\VMS> python manage.py migrate 

*)
(I already have created superuser='admin' with password='admin'. So following command may not be useful to you )

(venv) C:\Users\hi\my_project\VMS> python manage.py createsuperuser

*)
(venv) C:\Users\hi\my_project\VMS> python manage.py runserver

Now if you goto URL 'http://127.0.0.1:8000', you would see all endpoints.

*) Now open another terminal(a.k.a. command line) and perform individual test as described below:

NOTE: Make sure you are in virtual env. as described below.

*******************
C:\Users\hi>cd my_project

C:\Users\hi\my_project>venv\Scripts\activate

(venv) C:\Users\hi\my_project>

******************

Now go inside 'VMS\api' directory and type following commands:

(venv) C:\Users\hi\my_project> cd VMS\api

(venv) C:\Users\hi\my_project\VMS\api> python test_api1_vendors.py

This checks following endpoints:

POST /api/vendors/

GET /api/vendors/

GET /api/vendors/{vendor_id}/

PUT /api/vendors/{vendor_id}/

DELETE /api/vendors/{vendor_id}/


(venv) C:\Users\hi\my_project\VMS\api> python test_api2_purchase_orders.py

This checks following endpoints:

POST /api/purchase_orders/

GET /api/purchase_orders/

GET /api/purchase_orders/{po_id}/

PUT /api/purchase_orders/{po_id}/

DELETE /api/purchase_orders/{po_id}/

(venv) C:\Users\hi\my_project\VMS\api> python test_api3_backend_logic.py

This checks following endpoints:

GET /api/vendors/{vendor_id}/performance/

GET /api/vendors/{vendor_id}/performance/

PUT /api/purchase_orders/{po_id}/acknowledge/

-OR- you can run all of the above 3 test by going up 1 directory and simply typing:

(venv) C:\Users\hi\my_project\VMS> python manage.py test

*) I performed above test and output is given in file test_output.txt
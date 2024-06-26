from datetime import timedelta
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from api.models import Vendor

#To run test: ..\Vendor_Management_System_with_Performance_Metrics\VMS> python.exe .\manage.py test -v 2 api/test/
User = get_user_model()

# model & views test
class VendorModelTest(APITestCase):
    def setUp(self):
        self.model = Vendor
        self.user = User.objects.create(email="test@test.com", password="test_password")
        self.vendor_data = dict(
            name="Ash",
            contact_details="test contact details of Ash",
            address="test address of Ash",
            on_time_delivery_rate=0.85,
            quality_rating_avg=4.2,
            average_response_time=timedelta(days=2).total_seconds(),
            fulfillment_rate=0.90,
        )
        self.vendor = self.model.objects.create(**self.vendor_data)
        self.vendor_url = reverse("vendor_detail", args=[self.vendor.id])
        self.vendor_create_url = reverse("vendors_list")
        self.client = APIClient()  # authenticated user
        self.client.force_authenticate(user=self.user)
        self.unauthenticated_anonymous_client = APIClient()  # Unauthenticated user

    
    def test_model_url(self):
        response = self.client.get(self.vendor.get_absolute_url())
        self.assertEqual(
            response.status_code, 200, "Invalid absolute url configuration"
        )
    
    
    def test_list_vendors(self):
        self.vendor_create_url = reverse("vendors_list")
        response = self.client.get(self.vendor_create_url)
        #print("response.data=",response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_list_vendors_with_anonymous_user(self):
        self.vendor_create_url = reverse("vendors_list")
        response = self.unauthenticated_anonymous_client.get(self.vendor_create_url)
        #print("response.data=",response.data)# o/p->{'detail': ErrorDetail(string='Authentication credentials were not provided.', code='not_authenticated')}
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIsNone(response.data.get("results"))
        self.assertEqual(
            getattr(response.data.get("detail"), "code"), "not_authenticated"
        )
    
    def test_create_vendor(self):
        new_vendor_data = {
            "name": "Bob",
            "contact_details": "test contact details of Bob",
            "address": "test address of Bob",
        }
        response = self.client.post(
            self.vendor_create_url, data=new_vendor_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.model.objects.count(), 2)
        
    
    def test_create_vendors_with_anonymous_user(self):
        new_vendor_data = {
            "name": "Bob",
            "contact_details": "test contact details of Bob",
            "address": "test address of Bob",
        }
        response = self.unauthenticated_anonymous_client.post(
            self.vendor_create_url, data=new_vendor_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(self.model.objects.count(), 1)
        self.assertEqual(
            getattr(response.data.get("detail"), "code"), "not_authenticated"
        )
    
    def test_create_vendor_blank_data(self):
        new_vendor_data = {
            "name": "",
            "contact_details": "",
            "address": "",
        }
        response = self.client.post(
            self.vendor_create_url, data=new_vendor_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(self.model.objects.count(), 1)
    
    def test_retrieve_vendor(self):
        detail_url = reverse("vendor_detail", args=[self.vendor.id])
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.vendor_data["name"])
    
    def test_retrieve_vendor_with_anonymous_user(self):
        detail_url = reverse("vendor_detail", args=[self.vendor.id])
        response = self.unauthenticated_anonymous_client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            getattr(response.data.get("detail"), "code"), "not_authenticated"
        )
    
    def test_update_vendor(self):
        update_data = {
            "name": "Sam",
            "contact_details": "test contact details of Sam",
            "address": "test address of Sam",
        }
        detail_url = reverse("vendor_detail", args=[self.vendor.id])
        response = self.client.put(detail_url, data=update_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.vendor.refresh_from_db()
        self.assertEqual(self.vendor.name, update_data["name"])
    
    def test_update_vendor_with_anonymous_user(self):
        update_data = {
            "name": "Sam",
            "contact_details": "test contact details of Sam",
            "address": "test address of Sam",
        }
        detail_url = reverse("vendor_detail", args=[self.vendor.id])
        response = self.unauthenticated_anonymous_client.put(
            detail_url, data=update_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            getattr(response.data.get("detail"), "code"), "not_authenticated"
        )
    
    def test_delete_vendor(self):
        detail_url = reverse("vendor_detail", args=[self.vendor.id])
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.model.objects.count(), 0)

    def test_delete_vendor_with_anonymous_user(self):
        detail_url = reverse("vendor_detail", args=[self.vendor.id])
        response = self.unauthenticated_anonymous_client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            getattr(response.data.get("detail"), "code"), "not_authenticated"
        )
    
    def test_get_vendor_performance_metrics(self):
        # Make a GET request to the performance endpoint
        detail_url = reverse("vendor_performance", args=[self.vendor.id])
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn("on_time_delivery_rate", response.data)
        self.assertIn("quality_rating_avg", response.data)
        self.assertIn("average_response_time", response.data)
        self.assertIn("fulfillment_rate", response.data)

    def test_get_vendor_performance_metrics_with_anonymous_user(self):
        # Make a GET request to the performance endpoint
        detail_url = reverse("vendor_performance", args=[self.vendor.id])
        response = self.unauthenticated_anonymous_client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            getattr(response.data.get("detail"), "code"), "not_authenticated"
        )
    
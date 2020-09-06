from django.test import TestCase, Client
from django.urls import reverse
from address.models import Address, Counter
import json

class TestViews(TestCase):

    def setUp(self):
        client = Client()
        self.home_url = reverse('address-home')
        self.get_address_url_id = reverse('get-address-detail', args=[1])
        self.get_address_url_short = reverse('get-address-detail', args=["tierapp"])
        self.get_counter_url = reverse('counter', args=["tierapp"])
        self.address1 = Address.objects.create(
            address='https://tier.app',
            short="tierapp"
        )


    def test_home(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'address/address_form.html')

    def test_create_POST(self):
        response = self.client.post(self.home_url, {
            "address": "tier2.app",
            "short": "tier2av"
            })
        self.assertEquals(response.status_code, 302)

    def test_get_address(self):
        response = self.client.get(self.get_address_url_id)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'address/address_detail.html')
    
    def test_get_address(self):
        response = self.client.get(self.get_address_url_short)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json(), {"address": 'https://tier.app', "short": "tierapp"})
    
    def test_get_counter(self):
        response = self.client.get(self.get_counter_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json(), {"visits": 0})

        self.client.get(self.get_address_url_short)

        response2 = self.client.get(self.get_counter_url)
        self.assertEquals(response2.json(), {"visits": 1})
    
    def test_create_POST_no_data(self):
        response = self.client.post(self.home_url, {})
        self.assertNotEquals(response.status_code, 302)
        self.assertEquals(Address.objects.all().count(), 1)
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from address.views import AddressCreateView, AddressDetailView, get_address_detail

class TestUrls(SimpleTestCase):

    def test_home_is_resolved(self):
        url = reverse('address-home')
        self.assertEquals(resolve(url).func.view_class, AddressCreateView)
    
    def test_address_detail_is_resolved(self):
        url = reverse('address-detail', args=[1]) #Expecting a number
        self.assertEquals(resolve(url).func.view_class, AddressDetailView)

    def test_get_address_detail_is_resolved(self):
        url = reverse('get-address-detail', args=["a-string"])
        self.assertEquals(resolve(url).func, get_address_detail)
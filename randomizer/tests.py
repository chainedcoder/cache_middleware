from django.test import TestCase
from django.test import Client
from django.urls import reverse
import json

class CacheTestCase(TestCase):
    def test_caching(self):
        client = Client()

        #using the random-secret route we should get a distinct value
        self.assertNotEqual(client.get(reverse('random_secret')).json()['secret'],
                         client.get(reverse('random_secret')).json()['secret'])

        #using the cached_secret route we should get a cached value that should not change as long the timeout has not expired
        self.assertEqual(client.get(reverse('cached_secret')).json()['secret'],
                         client.get(reverse('cached_secret')).json()['secret'])
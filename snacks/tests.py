from django.test import TestCase

from django.test import TestCase 
from django.urls import reverse



class SnacksTests(TestCase):
    def test_snack_list_page_status_code(self):
        url = reverse('snack_list')
        actual_status_code = self.client.get(url).status_code
        expected_status_code = 200
        self.assertEqual(actual_status_code, expected_status_code)

        
    def test_snack_list_page_templete(self):
        url = reverse('snack_list')
        actual_status_code = self.client.get(url)
        self.assertTemplateUsed(actual_status_code, 'snack_list.html')
        self.assertTemplateUsed(actual_status_code, 'base.html')

   
    def test_not_found(self):
        url = '/snacks/hello'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
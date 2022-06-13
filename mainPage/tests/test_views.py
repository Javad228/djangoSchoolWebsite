from django.test import TestCase, Client
from django.urls import reverse
from users.models import User, Classes, Student, Instructor, Teaches, TeachesWithDate, Attendance

class TestViews(TestCase):

    def test_list_GET(self):
        client = Client()
        response = client.get(reverse('login'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')
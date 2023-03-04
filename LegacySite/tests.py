from django.test import TestCase
from LegacySite.models import Card
from django.test import Client
# Create your tests here.

class MyTest(TestCase):
    # Django's test run with an empty database. We can populate it with
    # data by using a fixture. You can create the fixture by running:
    #    mkdir LegacySite/fixtures
    #    python manage.py dumpdata LegacySite > LegacySite/fixtures/testdata.json
    # You can read more about fixtures here:
    #    https://docs.djangoproject.com/en/4.0/topics/testing/tools/#fixture-loading
    fixtures = ["testdata.json"]

    # Assuming that your database had at least one Card in it, this
    # test should pass.
    def test_case_1(self):
            response = self.client.get('/buy.html?director=<script>alert("Hello")</script>')
            if "<script>alert(1)</script>" in str(response.content):
                print("Failed")
                self.fail("script present")
            else:
                print("SUCCESS")
            
    def test_case_2(self):
        self.client = Client(enforce_csrf_checks=True)     
        response = self.client.post('gift.html?amount=1000&username=test2')
        self.assertEqual(response.status_code, 404)
        print("SUCCESS")
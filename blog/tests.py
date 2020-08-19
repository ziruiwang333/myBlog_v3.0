from django.test import TestCase
from .models import MyDetail
import datetime
# Create your tests here.

class MyDetailTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        MyDetail.objects.create(name = 'Zirui Wang', age = '22', date_of_birth='1998-11-28', phone1 = '+447718937880', email='zxw780@student.bham.ac.uk', country='United Kingdom', city='Birmingham', address='Selly Oak')
    
    def test_name(self):
        testQuery = MyDetail.objects.get(id=1)
        name = testQuery.name
        print("name: " + name)
        self.assertEquals(name, 'Zirui Wang')
    
    def test_age(self):
        testQuery = MyDetail.objects.get(id=1)
        age = testQuery.age
        print("age: " + age)
        self.assertEquals(age, '22')
    
    def test_date_of_birth(self):
        testQuery = MyDetail.objects.get(id=1)
        date = testQuery.date_of_birth
        print("date of birth: " + date.strftime("%Y-%m-%d"))
        self.assertEquals(date, datetime.date(*map(int, '1998-11-28'.split('-'))))
        
    def test_phone1(self):
        testQuery = MyDetail.objects.get(id=1)
        phone1 = testQuery.phone1
        print("phone1: " + phone1)
        self.assertEquals(phone1, '+447718937880')
        
    def test_phone2(self):
        testQuery = MyDetail.objects.get(id=1)
        phone2 = testQuery.phone2
        print("phone2: " + phone2)
        self.assertEquals(phone2, '')
        
    def test_email(self):
        testQuery = MyDetail.objects.get(id=1)
        email = testQuery.email
        print("email: " + email)
        self.assertEquals(email, 'zxw780@student.bham.ac.uk')
        
    def test_country(self):
        testQuery = MyDetail.objects.get(id=1)
        country = testQuery.country
        print("country: " + country)
        self.assertEquals(country, 'United Kingdom')
        
    def test_city(self):
        testQuery = MyDetail.objects.get(id=1)
        city = testQuery.city
        print("city: " + city)
        self.assertEquals(city, 'Birmingham')
       
    def test_address(self):
        testQuery = MyDetail.objects.get(id=1)
        address = testQuery.address
        print("address: " + address)
        self.assertEquals(address, 'Selly Oak')
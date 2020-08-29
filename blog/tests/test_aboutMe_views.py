from django.test import TestCase
from django.urls import reverse

from blog.models import *

class AuthorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        MyDetail.objects.create(name = 'Zirui Wang', age = '22', date_of_birth='1998-11-28', phone1 = '+447718937880', email='zxw780@student.bham.ac.uk', country='United Kingdom', city='Birmingham', address='Selly Oak')
        
        Education.objects.create(university = 'University of Birmingham', start_date = '2018-10-01', end_date = '2021-07-01', degree = 'Year3', college = 'School of Computer Science', subject = 'Computer Science')
        
        UoB_Year_1.objects.create(course = 'course1')
        UoB_Year_1.objects.create(course = 'course2')
        UoB_Year_1.objects.create(course = 'course3')
        UoB_Year_1.objects.create(course = 'course4')
        UoB_Year_1.objects.create(course = 'course5')
        
        UoB_Year_2.objects.create(course = 'course1')
        UoB_Year_2.objects.create(course = 'course2')
        UoB_Year_2.objects.create(course = 'course3')
        UoB_Year_2.objects.create(course = 'course4')
        UoB_Year_2.objects.create(course = 'course5')
        UoB_Year_2.objects.create(course = 'course6')
        
        UoB_Year_3.objects.create(course = 'course1')
        UoB_Year_3.objects.create(course = 'course2')
        UoB_Year_3.objects.create(course = 'course3')
        UoB_Year_3.objects.create(course = 'course4')
        UoB_Year_3.objects.create(course = 'course5')
        
        Work_Experience.objects.create(company_name = 'Goodwe', start_date = '2020-06-16', end_date = '2020-08-31', job_title = 'Software Testing Engineer', job_describe = 'test')
        
        Personal_Statement.objects.create(ps_describe = 'test test test')
        
        
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/introduction')
        self.assertEqual(response.status_code, 200)
        
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('introduction'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('introduction'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/introduction.html')
from django.test import TestCase
from blog.models import Work_Experience
import datetime

class WorkExperienceTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Work_Experience.objects.create(company_name = 'Goodwe', start_date = '2020-06-16', end_date = '2020-08-31', job_title = 'Software Testing Engineer', job_describe = 'test')
        
    def test_company_name(self):
        testQuery = Work_Experience.objects.get(id=1)
        company_name = testQuery.company_name
        print("company name: " + company_name)
        self.assertEquals(company_name, 'Goodwe')
        
    def test_company_name_max_length(self):
        testQuery = Work_Experience.objects.get(id=1)
        max_length = testQuery._meta.get_field('company_name').max_length
        print("company name max length: " + str(max_length))
        self.assertEquals(max_length, 200)
        
    def test_start_date(self):
        testQuery = Work_Experience.objects.get(id=1)
        start_date = testQuery.start_date
        print("job start_date: " + start_date.strftime("%Y-%m-%d"))
        self.assertEquals(start_date, datetime.date(*map(int, '2020-06-16'.split('-'))))
        
    def test_end_date(self):
        testQuery = Work_Experience.objects.get(id=1)
        end_date = testQuery.end_date
        print("job end_date: " + end_date.strftime("%Y-%m-%d"))
        self.assertEquals(end_date, datetime.date(*map(int, '2020-08-31'.split('-'))))
        
    def test_job_title(self):
        testQuery = Work_Experience.objects.get(id=1)
        job_title = testQuery.job_title
        print("job title: " + job_title)
        self.assertEquals(job_title, 'Software Testing Engineer')
        
    def test_job_title_max_length(self):
        testQuery = Work_Experience.objects.get(id=1)
        max_length = testQuery._meta.get_field('job_title').max_length
        print("job title max length: " + str(max_length))
        self.assertEquals(max_length, 200)
        
    def test_job_describe(self):
        testQuery = Work_Experience.objects.get(id=1)
        job_describe = testQuery.job_describe
        print("job describe: " + job_describe)
        self.assertEquals(job_describe, 'test')
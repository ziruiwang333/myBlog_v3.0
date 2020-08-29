from django.test import TestCase
from blog.models import Education
import datetime

class EducationTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Education.objects.create(university = 'University of Birmingham', start_date = '2018-10-01', end_date = '2021-07-01', degree = 'Year3', college = 'School of Computer Science', subject = 'Computer Science')
        
    def test_university(self):
        testQuery = Education.objects.get(id=1)
        university = testQuery.university
        print("university: " + university)
        self.assertEquals(university, 'University of Birmingham')
        
    def test_university_max_length(self):
        testQuery = Education.objects.get(id=1)
        max_length = testQuery._meta.get_field('university').max_length
        print("university max length: " + str(max_length))
        self.assertEquals(max_length, 200)
        
    def test_start_date(self):
        testQuery = Education.objects.get(id=1)
        start_date = testQuery.start_date
        print("university start date: " + start_date.strftime("%Y-%m-%d"))
        self.assertEquals(start_date, datetime.date(*map(int, '2018-10-01'.split('-'))))
        
    def test_end_date(self):
        testQuery = Education.objects.get(id=1)
        end_date = testQuery.end_date
        print("university end date: " + end_date.strftime("%Y-%m-%d"))
        self.assertEquals(end_date, datetime.date(*map(int, '2021-07-01'.split('-'))))
        
    def test_degree(self):
        testQuery = Education.objects.get(id=1)
        degree = testQuery.degree
        print("degree: " + degree)
        self.assertEquals(degree, 'Year3')
        
    def test_degree_max_length(self):
        testQuery = Education.objects.get(id=1)
        max_length = testQuery._meta.get_field('degree').max_length
        print("degree max length: " + str(max_length))
        self.assertEquals(max_length, 200)
        
    def test_college(self):
        testQuery = Education.objects.get(id=1)
        college = testQuery.college
        print("college: " + college)
        self.assertEquals(college, 'School of Computer Science')
        
    def test_college_max_length(self):
        testQuery = Education.objects.get(id=1)
        max_length = testQuery._meta.get_field('college').max_length
        print("college max length: " + str(max_length))
        self.assertEquals(max_length, 200)
        
    def test_subject(self):
        testQuery = Education.objects.get(id=1)
        subject = testQuery.subject
        print("subject: " + subject)
        self.assertEquals(subject, 'Computer Science')
        
    def test_subject_max_length(self):
        testQuery = Education.objects.get(id=1)
        max_length = testQuery._meta.get_field('subject').max_length
        print("subject max length: " + str(max_length))
        self.assertEquals(max_length, 200)
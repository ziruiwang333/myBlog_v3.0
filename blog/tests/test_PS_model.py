from django.test import TestCase
from blog.models import Personal_Statement
import datetime

class PSTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Personal_Statement.objects.create(ps_describe = 'test test test')
        
    
    def test_ps_describe(self):
        testQuery = Personal_Statement.objects.get(id=1)
        ps_describe = testQuery.ps_describe
        print("personal statement: " + ps_describe)
        self.assertEquals(ps_describe, 'test test test')


from django.test import TestCase
import datetime as dt 
from .models import Image, Profile
from django.contrib.auth.models import User





# Create your tests here.

class ImageTestClass(TestCase):

    def setUp(self):
        self.image = Image(image ='imageurl', image_name='nature', image_caption='wowo', likes=200, comments='wonderful')

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

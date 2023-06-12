from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
 

class Place(models.Model):
    place = models.CharField(max_length=200)

    def __str__(self):
        return self.place
    
class Activity(models.Model):
    activity = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.activity
    
class Adventure(models.Model):
    title = models.CharField(verbose_name="Heading",max_length=300)
    image1 = CloudinaryField('image' ,blank=True)
    image2 = CloudinaryField('image',blank=True)
    image3 = CloudinaryField('image',blank=True)
    image4 = CloudinaryField('image',blank=True)
    image5 = CloudinaryField('image',blank=True)
    desc = RichTextField()
    place = models.ForeignKey(Place,on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity,on_delete=models.CASCADE,default="Hiking")

    def __str__(self) :
        return f"{self.title},{self.place}"

class Status(models.Model):
    status = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.status
Language = (
    ("English","English"),
    ("Hindi","Hindi"),
    ("Local","Local"),
)
Gender = (
    ("Male","Male"),
    ("Female","Female"),
    ("Other","Other"),
)

class Guide(models.Model):
    Username = models.CharField(max_length=200)
    guide_image = CloudinaryField('guide_image')

    mob_number =models.IntegerField()
    Addhar_number= models.IntegerField()
    Email_id = models.EmailField()
    Guide_location = models.ForeignKey(Place,on_delete=models.CASCADE)
    Address = models.TextField()
    language = models.CharField(max_length=200,choices=Language)
    gender = models.CharField(max_length=200,choices=Gender)
    price = models.PositiveIntegerField(blank=True,null=True)

    guide_proffesion = models.ForeignKey(Activity,on_delete=models.CASCADE)
    status = models.ForeignKey(Status,on_delete=models.CASCADE,default="User")

class Help(models.Model):
    username = models.CharField(max_length=288)
    email = models.CharField(max_length=288)
    problem = models.TextField()

class Offers(models.Model):
    place = models.ForeignKey(Adventure,on_delete=models.CASCADE)
    Duration=models.IntegerField()
    Price=models.IntegerField()
    Description=models.TextField()



from django.db import models



# Create your models here.
class Userdetails(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)

class Status(models.Model):
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    description=models.TextField()
    upload_time=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='images/')
    user=models.ForeignKey(Userdetails, on_delete=models.CASCADE, related_name='status')
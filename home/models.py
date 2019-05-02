from django.db import models
from stdimage import StdImageField



# Create your models here.
class Intro(models.Model):
    ijudul = models.CharField(max_length=50)
    iisi = models.TextField(blank=True)
    ifoto = StdImageField(upload_to="home/static/images/",null=True,blank=True, variations={'thumbnail': (9000, 900)})


class Services(models.Model):
    sjudul = models.CharField(max_length=50)
    sisi = models.TextField(blank=True)
    sfoto = StdImageField(upload_to="home/static/images/",null=True,blank=True, variations={'thumbnail': (600, 600)})

class Works(models.Model):
    wfoto = StdImageField(upload_to="home/static/images/", blank=True, null=True, variations={'thumbnail': (600, 600)})

class Testi(models.Model):
    tnama = models.CharField(max_length=30)
    tisi = models.TextField(max_length=600)






    

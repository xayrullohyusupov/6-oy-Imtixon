from django.db import models

class Indeximage(models.Model):
    img = models.ImageField(upload_to='blog-img/')

class Message(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Index(models.Model):
    img = models.ImageField(upload_to='blog_img2/')
    name = models.CharField(max_length=15)
    title = models.CharField(max_length=12)
    category = models.TextField()

    def __str__(self):
        return self.title

class Index_Banner(models.Model):
    image = models.ImageField(upload_to='index_banner/')
    category = models.TextField()
    name = models.CharField(max_length=20)
    title = models.TextField(max_length=15)

    def __str__(self):
        return self.name
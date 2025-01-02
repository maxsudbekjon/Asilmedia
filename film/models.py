from django.db import models
from django.db.models import Model, CharField, TextField, ManyToManyField, ForeignKey, CASCADE, SET_NULL, DateField, \
    IntegerField, BooleanField, FileField, ImageField, DateTimeField


# Create your models here.
class Actor(Model):
    name=CharField(max_length=100)

    def __str__(self):
        return self.name
class Genre(Model):
    name=CharField(max_length=255)
    def __str__(self):
        return self.name
class Director(Model):
    name=CharField(max_length=255)
    def __str__(self):
        return self.name
class Comment(Model):
    user=ForeignKey('user.User',on_delete=SET_NULL,null=True,blank=True)
    text=TextField()
    date=DateField(auto_now_add=True)
    like_count=IntegerField(default=0)
    dis_like_count=IntegerField(default=0)
    like=BooleanField(default=False)
    dis_like=BooleanField(default=False)
    film=ForeignKey('film.Film',on_delete=SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.user
class Film(Model):
    name=CharField(max_length=255)
    description=TextField()
    actor=ManyToManyField('film.Actor',related_name='films')
    genre=ManyToManyField('film.Genre',related_name='films')
    director=ManyToManyField('film.Director',related_name='films')
    country=CharField(max_length=255)
    year=DateField()
    time=IntegerField(default=0)
    video=FileField(upload_to='film/%Y/%m/%d')
    image=ImageField(upload_to='film/%Y/%m/%d')
    translate_time=DateTimeField(auto_now_add=True)
    views_count=IntegerField(default=0)
    like_count = IntegerField(default=0)
    dis_like_count = IntegerField(default=0)
    like = BooleanField(default=False)
    dis_like = BooleanField(default=False)
    def __str__(self):
        return self.name

class Saved(Model):
    film=ForeignKey('film.Film',on_delete=SET_NULL,null=True,blank=True)
    user=ForeignKey('user.User',on_delete=CASCADE)
    def __str__(self):
        return self.film.name




from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def validate_registration(self, post_data):
        errors={}
        if len(post_data['first_name'])<2:
            errors['first_name']= "First name must be at least 2 characters"
        if len(post_data['last_name']) < 2:
            errors['last_name']= "Last name must be at least 2 characters"
        if len(post_data['email']) == 0:
            errors['email']="Email must be provided"
        if len(post_data['password']) ==0:
            errors['password']="Password must be provided"
        emails_query = self.filter(email=post_data['email'])
        if len(emails_query) >0:
            errors['email'] = "User with that email already exists"
        if post_data['password'] != post_data['password_confirmation']:
            errors['password_confirmation'] = "Passwords do not match"
        return errors

class UserManager2(models.Manager):
    def validate_registration(self, post_data):
        errors={}
        if len(post_data['first_name'])<2:
            errors['first_name']= "First name must be at least 2 characters"
        if len(post_data['last_name']) < 2:
            errors['last_name']= "Last name must be at least 2 characters"
        if len(post_data['email']) == 0:
            errors['email']="Email must be provided"
        emails_query = self.filter(email=post_data['email'])
        if len(emails_query) >0 :
            errors['email'] = "User with that email already exists"
        return errors

class UserManager3(models.Manager):
    def validate_registration(self, post_data):
        errors={}
        if len(post_data['first_name'])<2:
            errors['first_name']= "First name must be at least 2 characters"
        if len(post_data['last_name']) < 2:
            errors['last_name']= "Last name must be at least 2 characters"
        if len(post_data['email']) == 0:
            errors['email']="Email must be provided"
        return errors

class User(models.Model):
    first_name= models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.CharField(max_length=45)
    password=models.CharField(max_length=255)
    objects = UserManager()
    objects2=UserManager2()
    objects3=UserManager3()

class QuoteManager(models.Manager):
     def validate_quote(self, post_data):
        errors={}
        if len(post_data['author'])<4:
            errors['author']= "Author name must be more than 3 characters"
        if len(post_data['content']) < 11:
            errors['content']= "Quote must be more than 10 characters"
        return errors

class Quote(models.Model):
    author= models.CharField(max_length=45)
    content=models.TextField(max_length=45)
    uploader=models.ForeignKey(User,related_name="quotes")
    likes=models.ManyToManyField(User, related_name="liked_quotes")
    objects=QuoteManager()
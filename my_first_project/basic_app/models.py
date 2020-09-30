from django.db import models
from django.contrib.auth.models import User #this is for last class

class Topic(models.Model):
    Top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.Top_name

class WebPage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=264,unique=True)
    url =  models.URLField(unique = True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage,on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


# the code below if from fifth lecture of Django
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # with the above line, the "user" has an one to one mapping wth the django in-built "User" module
    #i.e. Username, Email, Password, First Name, Last NAME
    # Directly inheriting from "User" class in UserProfileInfo is not good practice
    # that is why we have done onetoone mapping. Now we will add some more columns of our wish to the "User" class

    portfolio = models.URLField (blank = True)
    profile_pic = models.ImageField(upload_to = 'profile_pics',blank=True)

    def __str__(self):
        return self.user.username
        # where username is coming from the default username column of Django User class

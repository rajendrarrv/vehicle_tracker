from django.db import models


# Create your models here.
class User(models.Model):
    name_text = models.CharField(max_length=21)
    email_text = models.CharField(max_length=50, unique=True, null=True)
    mobile_no_text = models.CharField(max_length=12, unique=True, null=True)
    password_text = models.CharField(max_length=10, null=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name_text

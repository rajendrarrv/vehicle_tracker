from django.db import models


# Create your models here.
class User(models.Model):
    name_text = models.CharField(max_length=20)
    email_text = models.CharField(max_length=20, unique=True)
    mobile_no_text = models.CharField(max_length=12, unique=True)
    pub_date = models.DateTimeField('date published')
    password_text = models.CharField(max_length=20);

    def __str__(self):
        return self.name_text

from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Programming(models.Model):
    fullname = models.CharField(max_length=100)
    std_code = models.CharField(max_length=15)
    mobile = models.CharField(max_length=13)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
from django.db import models
class flower(models.Model):
    name=models.CharField(max_length=250)
    sname=models.CharField(max_length=250)
    desc=models.TextField()
    img=models.ImageField(upload_to='garden')

    def __str__(self):
        return self.name

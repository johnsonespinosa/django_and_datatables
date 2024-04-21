from django.db import models


class Programmer(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=3)   
    score = models.PositiveSmallIntegerField()
    birthday = models.DateField()
    
    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'

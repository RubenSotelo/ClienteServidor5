from django.db import models

# Create your models here.

class Example1(models.Model):
    name = models.CharField(max_length = 255, null = False),
    curp = models.CharField(max_length = 16, null = False),
    direccion = models.CharField(max_length = 200, null = False),
    edad = models.IntegerField(null  = False),
    
    def __str__(self):
        return self.name, self.curp, self.direccion, self.edad

    class Mate:
        db_table = 'Example1'

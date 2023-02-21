from django.db import models

# Create your models here.
class BasicForm(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    bday = models.DateField()
    
    class Meta:
        db_table = 'Form_data'
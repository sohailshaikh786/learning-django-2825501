from django.db import models

class Pet(models.Model):
    SEX_CHOICE = [('M','Male'),('F','Female')]
    name = models.CharField(max_length=100)
    submittor = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30,blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=1,choices = SEX_CHOICE,blank=True)
    submission_date =models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('Vaccine',blank=True)


    
class Vaccine(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self) :
        return self.name
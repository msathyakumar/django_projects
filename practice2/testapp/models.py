from django.db import models

# Create your models here.
class RegisterModel(models.Model):
    Reg_id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30)
    choices_fields = [('ECE','Electronics'),('CSE','Computers'),('MECH','mechanics'),('EEE','Electrics')]
    Branch = models.CharField(max_length=4,choices=choices_fields)
    class Meta:
        ordering=['Reg_id']
    def __str__(self):
        return self.Name

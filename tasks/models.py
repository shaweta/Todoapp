from django.db import models

# Create your models here.
class Tasks(models.Model):
    task_name=models.CharField(max_length=100)
    is_completed=models.BooleanField(default=False)
    due_date=models.DateField()
    created_on=models.DateTimeField(auto_now=True)
    updated_on=models.DateTimeField(auto_now=True)

    class Meta:
         ordering=["-updated_on"]
    def __str__(self) :
        return self.task_name
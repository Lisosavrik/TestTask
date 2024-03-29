from django.db import models

class Projects(models.Model):
    project_id = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    status = models.CharField(max_length=20)
    sector = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title







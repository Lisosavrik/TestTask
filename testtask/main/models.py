from django.db import models

class Projects(models.Model):
    project_id = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    date = models.DateField()
    status = models.CharField(max_length=200)
    sector = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    p_type = models.CharField(max_length=200)

    def __str__(self):
        return self.title







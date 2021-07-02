from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ForeignKey

class Role(models.Model):
    USER_ROLE = [
        ('HDC', 'HDC'),
        ('Pelamar', 'Pelamar'),
        ('Korektor', 'Korektor'),
    ]

    role = models.CharField(
    max_length=10,
    choices=USER_ROLE,
    default='Pelamar')
    
    def __str__(self):
        return self.role

class Test(models.Model):
    test_name = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return self.test_name
        
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Job(models.Model):
    job_name = models.CharField(max_length=100)
    description = models.TextField()
    hdc_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tests = models.ManyToManyField(Test)

    def __str__(self):
        return self.job_name

class JobList(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null = True)
    pelamar_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    JOB_STATUS = [
        ('review', 'review'),
        ('diterima', 'diterima'),
        ('ditolak', 'ditolak'),
    ]

    status = models.CharField(
            max_length=10,
            choices=JOB_STATUS,
            default='review',
            null = True)
    tests = models.ManyToManyField(Test)

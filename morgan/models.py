from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Project(models.Model):
    project_id = models.IntegerField(unique=True, validators=[MaxValueValidator(9999), MinValueValidator(1)])
    name = models.CharField(max_length=25, null=False, blank=False)
    budget = models.FloatField(max_length=8, null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    statusOptions = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Complete', 'Complete'),
    )
    status = models.CharField(max_length=8, choices=statusOptions, null=False, blank=False)
    notes = models.CharField(max_length=100, null=True, blank=True)

class Department(models.Model):
    department_id = models.IntegerField(unique=True, validators=[MaxValueValidator(99), MinValueValidator(1)])
    name = models.CharField(max_length=30, null=False, blank=False)
    location = models.CharField(max_length=30, null=False, blank=False)

class Employee(models.Model):
    employee_id = models.IntegerField(unique=True, validators=[MaxValueValidator(999), MinValueValidator(1)])
    lastname = models.CharField(max_length=25, null=False, blank=False)
    firstname = models.CharField(max_length=25, null=False, blank=False)
    street_address = models.CharField(max_length=50, null=False, blank=False)
    suburb = models.CharField(max_length=15, null=False, blank=False)
    hourly_rate = models.FloatField(validators=[MaxValueValidator(75.00), MinValueValidator(10.00)], null=False, blank=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, to_field='department_id', null=True)

class Assignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, to_field='employee_id', null=True)
    employee = models.ForeignKey(Project, on_delete=models.CASCADE, to_field='project_id', null=True)
    hours = models.IntegerField(validators=[MaxValueValidator(150), MinValueValidator(1)], null=False, blank=False)

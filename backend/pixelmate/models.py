from django import forms
from django.forms import DateField
from djongo import models
from datetime import datetime

# Create your models here.


class Signup(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Username = models.CharField(max_length=30)
    Email = models.CharField(max_length=50)
    Password = models.CharField(max_length=16)


class Login(models.Model):
    Id = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=30)
    Email = models.CharField(max_length=50)


class Tech(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        abstract = True


class TechForm(forms.ModelForm):
    class Meta:
        model = Tech
        fields = (
            'name',
        )


class ProjectOnGoing(models.Model):
    Id = models.AutoField(primary_key=True)
    Username = models.ForeignKey(
        Signup, on_delete=models.CASCADE, default=1)
    Name = models.CharField(max_length=30)
    Description = models.CharField(max_length=50)
    CreatedDate = models.DateTimeField(default=datetime.now, blank=True)
    Url = models.CharField(max_length=50)
    Technology = models.ArrayField(
        model_container=Tech,
        model_form_class=TechForm
    )


class Work(models.Model):
    Title = models.CharField(max_length=100)
    Date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        abstract = True


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ('Title', 'Date'
                  )


class ProjectCompleted(models.Model):
    Id = models.AutoField(primary_key=True)
    Username = models.ForeignKey(
        Signup, on_delete=models.CASCADE, default=1)
    Name = models.CharField(max_length=30)
    Description = models.CharField(max_length=50)
    CreatedDate = models.DateTimeField(default=datetime.now, blank=True)
    CompletedDate = models.DateTimeField(default=datetime.now, blank=True)
    Work = models.ArrayField(
        model_container=Work,
        model_form_class=WorkForm
    )
    Url = models.CharField(max_length=50)
    Technology = models.ArrayField(
        model_container=Tech,
        model_form_class=TechForm
    )


class Task(models.Model):
    Id = models.AutoField(primary_key=True)
    Project = models.ForeignKey(
        ProjectOnGoing, on_delete=models.CASCADE, default=1)
    Title = models.CharField(max_length=100)
    Date = models.DateTimeField(default=datetime.now, blank=True)

from django.db import models
from django import forms
from django.core.validators import FileExtensionValidator



# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=30) 
    def __str__(self):
        return self.name  


class Rules(models.Model):
    docfile = models.FileField(upload_to='biblio', validators=[FileExtensionValidator(['yar'])] )
    tags = models.ManyToManyField(Tags, related_name='files')


class RulesForm(forms.Form):
    docfile = forms.FileField(label='Ajouter une regle')
    tags= forms.ModelMultipleChoiceField(queryset=Tags.objects.all())

class TagsForm(forms.Form):
    name = forms.CharField(max_length=100)




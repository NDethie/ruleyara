# Generated by Django 3.0.7 on 2020-06-23 08:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yararule', '0004_rules_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rules',
            name='docfile',
            field=models.FileField(upload_to='biblio', validators=[django.core.validators.FileExtensionValidator(['yara'])]),
        ),
        migrations.AlterField(
            model_name='rules',
            name='tags',
            field=models.ManyToManyField(related_name='files', to='yararule.Tags'),
        ),
    ]
# Generated by Django 5.1.4 on 2025-01-09 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

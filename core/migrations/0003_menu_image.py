# Generated by Django 5.2.4 on 2025-07-24 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_employee_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='menu_images/'),
        ),
    ]

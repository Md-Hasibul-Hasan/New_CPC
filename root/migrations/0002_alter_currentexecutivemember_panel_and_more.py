# Generated by Django 5.2 on 2025-06-15 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentexecutivemember',
            name='panel',
            field=models.CharField(choices=[('Admin Panel', 'Admin Panel'), ('Mentor Wing', 'Mentor Wing'), ('IT Wing', 'IT Wing'), ('Executive Wing', 'Executive Wing'), ('Advertising & Finance Management Wing', 'Advertising & Finance Management Wing'), ('Public Relations Wing', 'Public Relations Wing')], max_length=100),
        ),
        migrations.AlterField(
            model_name='formerexecutivemember',
            name='panel',
            field=models.CharField(choices=[('Admin Panel', 'Admin Panel'), ('Mentor Wing', 'Mentor Wing'), ('IT Wing', 'IT Wing'), ('Executive Wing', 'Executive Wing'), ('Advertising & Finance Management Wing', 'Advertising & Finance Management Wing'), ('Public Relations Wing', 'Public Relations Wing')], max_length=100),
        ),
    ]

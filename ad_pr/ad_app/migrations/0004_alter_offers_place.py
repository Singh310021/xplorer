# Generated by Django 4.1.5 on 2023-06-08 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ad_app', '0003_offers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ad_app.adventure'),
        ),
    ]

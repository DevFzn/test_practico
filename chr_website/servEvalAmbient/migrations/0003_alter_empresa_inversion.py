# Generated by Django 4.1.7 on 2023-02-21 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servEvalAmbient', '0002_alter_empresa_inversion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='inversion',
            field=models.CharField(max_length=255),
        ),
    ]
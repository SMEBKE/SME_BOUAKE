# Generated by Django 5.1 on 2024-08-09 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('santementale', '0002_remove_patient_id_alter_patient_code_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suivipatient',
            name='molecule',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='suivipatient',
            name='type_molecule',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
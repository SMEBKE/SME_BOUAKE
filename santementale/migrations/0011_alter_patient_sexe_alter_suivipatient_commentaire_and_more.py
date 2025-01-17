# Generated by Django 5.1 on 2024-09-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('santementale', '0010_alter_suivipatient_code_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='sexe',
            field=models.CharField(blank=True, choices=[('F', 'FEMME'), ('H', 'HOMME'), ('M', 'HOMME'), ('FE', 'FE'), ('FA', 'FA')], max_length=2),
        ),
        migrations.AlterField(
            model_name='suivipatient',
            name='commentaire',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='suivipatient',
            name='date_etat',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='suivipatient',
            name='dotation',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='suivipatient',
            name='etat_patient',
            field=models.CharField(blank=True, choices=[('DCD', 'DECEDE'), ('TRANS-OUT', 'TRANSFERE-OUT'), ('TRANS-IN', 'TRANSFERE-IN'), ('REFUS', 'REFUS VOLONTAIRE'), ('AUTRES', 'AUTRES')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='suivipatient',
            name='molecule',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='suivipatient',
            name='nb_molecule',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='suivipatient',
            name='type_molecule',
            field=models.CharField(blank=True, choices=[('ANTI-DEPRESSIF', 'ANTI-DEPRESSIF'), ('ANTI-PSYCHOTIQUE', 'ANTI-PSYCHOTIQUE'), ('ANTI-EPILEPTIQUE', 'ANTI-EPILEPTIQUE'), ('AUTRES', 'AUTRES')], max_length=25, null=True),
        ),
    ]

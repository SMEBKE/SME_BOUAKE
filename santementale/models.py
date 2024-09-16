from django.db import models

# Create your models here.
# Begin models patient.

class Patient(models.Model):
    CHOIX_PATHOLOGIE = [
        ('DEPRESSION', 'DEPRESSION'),
        ('EPILEPSIE', 'EPILEPSIE'),
        ('PSYCHOSE', 'PSYCHOSE')  
    ]

    CHOIX_SEXE = [
        ('F', 'FEMME'),
        ('H', 'HOMME'),
        ('M', 'HOMME'),
        ('FE', 'FE'),
        ('FA', 'FA') 
    ]

    CHOIX_CDS = [
        ('LANGUIBONOU', 'CSU LANGUIBONOU'),
        ('BOTRO', 'HG BOTRO'),
        ('KROFOINSOU', 'CSR KROFOINSOU'),
        ('FARI', 'CSR FARI MBABO'),
        ('BODOKRO', 'CSU BODOKRO'),
        ('MARABA', 'CSU MARABADJASSA'),
        ('ANDO', 'CSU ANDO-KEKRENOU'),
        ('POKOUKRO', 'CSU NGUESSAN POKOUKRO'),
        ('ASSANDRE', 'CSR ASSANDRE') 
    ]

    code_patient = models.CharField(max_length=30,primary_key=True)
    sexe = models.CharField(max_length=2, choices=CHOIX_SEXE, blank=True)
    age = models.IntegerField()
    pathologie = models.CharField(max_length=15, choices=CHOIX_PATHOLOGIE, blank=True)
    centre_sante = models.CharField(max_length=50, choices=CHOIX_CDS, blank=True)
    date_admission = models.DateField(null = True)

    # Affichage champs
    def __str__(self):
        return self.code_patient

# End models patient.

# Begin models Suivipatient.

class Suivipatient(models.Model):
    CHOIX_TYPE_MOL = [
        ('ANTI-DEPRESSIF', 'ANTI-DEPRESSIF'),
        ('ANTI-PSYCHOTIQUE', 'ANTI-PSYCHOTIQUE'),
        ('ANTI-EPILEPTIQUE', 'ANTI-EPILEPTIQUE'),
        ('AUTRES', 'AUTRES')  
    ]

    CHOIX_MOL = [
        ('PHENOBARBITAL', 'PHENOBARBITAL'),
        ('PHENYTOINE', 'PHENYTOINE'),
        ('CARBAMAZEPINE', 'CARBAMAZEPINE'),
        ('VALPROATE SE SODIUM', 'VALPROATE SE SODIUM'),
        ('LEVETIRACETAM', 'LEVETIRACETAM'),
        ('OLANZAPINE', 'OLANZAPINE'),
        ('RISPERIDONE', 'RISPERIDONE'),
        ('HALOPERIDOL', 'HALOPERIDOL'),
        ('CHLORPROMAZINE', 'CHLORPROMAZINE'),
        ('HALOPERIDOL DECANOATE', 'HALOPERIDOL DECANOATE'),
        ('AMYTRIPTYLINE', 'AMYTRIPTYLINE'),
        ('FLUOXETINE', 'FLUOXETINE'),
        ('PAROXETINE', 'PAROXETINE'),
        ('SERTALINE', 'SERTALINE'),
        ('TRIHEXYPHENIDYL (ARTANE)', 'ARTANE'),
        ('PROMETHAZINE', 'PROMETHAZINE')  
    ]

    CHOIX_ETAT_PATIENT = [
        ('DCD', 'DECEDE'),
        ('TRANS-OUT', 'TRANSFERE-OUT'),
        ('TRANS-IN', 'TRANSFERE-IN'),
        ('REFUS', 'REFUS VOLONTAIRE'),
        ('AUTRES', 'AUTRES')  
    ]

    #code_patient = models.ManyToManyField(Patient, blank=True)
    #author = models.ForeignKey(Author, on_delete=models.CASCADE)
    code_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_derniere_visite = models.DateField()
    dotation = models.IntegerField(null = True, blank = True)
    nb_molecule = models.IntegerField(null = True, blank = True)
    type_molecule = models.CharField(max_length=25, choices=CHOIX_TYPE_MOL, null = True, blank = True)
    molecule = models.CharField(max_length=50, null = True, blank = True)
    etat_patient = models.CharField(max_length=20, choices=CHOIX_ETAT_PATIENT, null = True, blank = True)
    date_etat = models.DateField(null = True, blank = True)
    commentaire = models.TextField(max_length=100,null = True, blank = True)
    # Affichage champs
    #def __str__(self):
       # return self.commentaire

# End models Suivipatient.

"""class Fruits(models.Model):
    CHOIX_FRUITS = [
        ('M', 'Mangue'),
        ('B', 'Banane'),
        ('O', 'Orange'),
    ]
    
    fruits = models.CharField(max_length=10, choices=CHOIX_FRUITS, default='M,B', blank=True)

    def __str__(self):
        return f"Fruits choisis: {', '.join(self.get_fruits_display())}" """

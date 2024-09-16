from django import forms
from .models import Suivipatient

class SuivipatientAdminForm(forms.ModelForm):
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
    
    molecule = forms.MultipleChoiceField(
        choices=CHOIX_MOL,
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = Suivipatient
        fields = '__all__'

    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        return ",".join(tags)  # Convertir la liste en chaîne de caractères


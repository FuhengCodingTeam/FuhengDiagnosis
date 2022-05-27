from django import forms

lastTreatment_CHOICES =( 
('same','Sale'),
('better','Better'),
('worse', 'Worse')
)

class lastTreatmentForm(forms.ModelForm):
    lastTreatment_live = forms.ChoiceField(choices=lastTreatment_CHOICES, widget=forms.RadioSelect())
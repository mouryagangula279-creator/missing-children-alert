from django import forms
from .models import MissingChild


class MissingChildForm(forms.ModelForm):

    class Meta:
        model = MissingChild

        fields = [
            'child_name',
            'age',
            'gender',
            'date_last_seen',
            'location_last_seen',
            'description',
            'guardian_name',
            'guardian_contact',
        ]

        widgets = {
            'child_name': forms.TextInput(attrs={
                'placeholder': 'Enter child name'
            }),

            'age': forms.NumberInput(attrs={
                'placeholder': 'Enter age',
                'min': '0'
            }),

            'gender': forms.Select(),

            'date_last_seen': forms.DateInput(attrs={
                'type': 'date'
            }),

            'location_last_seen': forms.TextInput(attrs={
                'placeholder': 'Enter last seen location'
            }),

            'description': forms.Textarea(attrs={
                'placeholder': 'Enter relevant identifying information',
                'rows': 4
            }),

            'guardian_name': forms.TextInput(attrs={
                'placeholder': 'Enter guardian name'
            }),

            'guardian_contact': forms.TextInput(attrs={
                'placeholder': 'Enter guardian contact number'
            }),
        }
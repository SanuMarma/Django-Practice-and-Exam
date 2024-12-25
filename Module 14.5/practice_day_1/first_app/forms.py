from django import forms
from django.forms.widgets import NumberInput
import datetime

class contactForm(forms.Form):
    name = forms.CharField(max_length=25, label='Full Name')
    email = forms.EmailField(label="Please enter your email address")
    roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number") 
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    # file = forms.FileField()
    agree = forms.BooleanField(label='Are you agree?')

    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))


    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)

    FOOD = [('B', 'Biriyani'), ('P', 'Pizza'), ('I', 'Ice Cream')]
    favorite_food = forms.MultipleChoiceField(choices=FOOD, widget=forms.CheckboxSelectMultiple)


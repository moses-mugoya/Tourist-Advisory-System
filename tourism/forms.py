from django import forms
from django.forms import DateInput
from django_countries import Countries

from .models import Expenses


class QuestionForm(forms.Form):
    CHOICE1 = [
        ('bus', 'By Bus'),
        ('car', 'By Car'),
        ('major_airline', 'By Major Airline'),
        ('low_cost_airline', 'By Low Cost Airline'),
        ('train', 'By Train')
    ]
    CHOICE2 = [
        ('business', 'Business Vacation'),
        ('academic', 'Academic Travel'),
        ('honeymoon', 'Honeymoon'),
        ('fun', 'Fun')
    ]
    CHOICE3 = [
        ('family', 'Family members'),
        ('friends', 'Friends'),
        ('work_mates', 'Work mates'),
        ('alone', 'Alone')
    ]
    CHOICE4 = [
        ('employed', 'Employed'),
        ('self_employed', 'Self Employed'),
        ('retired', 'Retired'),
        ('student', 'Student')
    ]
    CHOICE5 = [
        ('rainy', 'Rainy'),
        ('sunny', 'Sunny'),
        ('cool', 'Cool temperatures')
    ]
    CHOICE6 = [
        ('height', 'Height Phobia'),
        ('water', 'Water Phobia'),
        ('animal', 'Animal Phobia'),
        ('none', 'None')
    ]
    CHOICE7 = [
        ('hiking', 'Hiking'),
        ('swimming', 'Swimming'),
        ('sight', 'Sight seeing')
    ]
    country = forms.ChoiceField(label='Please select your country', widget=forms.Select, choices=Countries)
    reason = forms.ChoiceField(choices=CHOICE2, widget=forms.RadioSelect, label='What are your reasons for the visit?')
    accompany = forms.ChoiceField(choices=CHOICE3, widget=forms.Select, label='Who is accompanying you?')
    spend = forms.CharField(label='How much do you plan to spend?', widget=forms.TextInput)
    phobia = forms.ChoiceField(choices=CHOICE6, widget=forms.Select, label='Do you have any phobia?')
    activity = forms.ChoiceField(choices=CHOICE7, widget=forms.RadioSelect, label='Which activity do you enjoy doing?')
    

class ExpenseForm(forms.ModelForm):
    CHOICE = [
        ('hiking', 'Hiking'),
        ('swimming', 'Swimming'),
        ('sight', 'Sight seeing'),
        ('skating', 'Skating'),
        ('Fun', 'Just fun')

    ]

    activity = forms.ChoiceField(choices=CHOICE, widget=forms.Select, label='Which activity do you plan to do?')
    tour_start_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}), label='Which day does your tour begin?')
    tour_end_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}), label='Which day does your tour end?')
    number_of_people = forms.IntegerField(widget=forms.NumberInput, label='How many people will you be travelling along with?')
    amount_to_spend = forms.IntegerField(widget=forms.NumberInput, label='How much do you plan to spend on food and other expenses like room service?')

    class Meta:
        model = Expenses
        fields = ('tour_start_date', 'tour_end_date', 'number_of_people', 'activity', 'amount_to_spend')








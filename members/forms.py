
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from .models import Member, Location, Lease, Soft_Service, Safety_Service, Hard_Service

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class MemberForm(forms.ModelForm):
    class Meta: 
        model = Member
        fields = ['text', 'phone_num', 'ceo_name', 'num_employees', 'maintenance_schedule']
        

class LocationForm(forms.ModelForm):
    class Meta: 
        model = Location 
        fields = ['text', 'address2', 'city', 'state', 'zipcode']

class LeaseForm(forms.ModelForm):
    class Meta: 
        model = Lease
        fields = ['text', 'rate', 'location', 'date']

class Soft_ServiceForm(forms.ModelForm):
    class Meta: 
        model = Soft_Service
        fields = ['text', 'security_crew_title', 'cleaning_crew_title', 'landscaping_crew_title', 'caterer']

class Safety_ServiceForm(forms.ModelForm):
    class Meta: 
        model = Safety_Service
        fields = ['text','training_schedule', 'audit_schedule', 'safety_meetings', 'safety_coordinator', 'job_safety_analysis']

class Hard_ServiceForm(forms.ModelForm):
    class Meta: 
        model = Hard_Service
        fields = ['text', 'electric_provider', 'plumbing_provider', 'hvac_provider', 'mechanical_provider', 'fire_safety_provider']
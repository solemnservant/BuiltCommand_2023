from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    #A Member is composed of the company general info
    text = models.CharField('Office Name',default = 'Office Name', max_length = 200)
    phone_num = models.CharField('Phone Number', default = '000-000-000', max_length = 12)
    ceo_name = models.CharField ('CEO', max_length = 50)
    num_employees = models.IntegerField('Number of Employees', default = 0)
    maintenance_schedule = models.CharField('maintenance schedule', max_length = 100)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Location(models.Model):
    #Location holds headquarters and satellite facilities info
    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    address = models.CharField('Address', default = 'Address', max_length = 250)
    address2 = models.CharField('Address_2',  default = 'Address_2', max_length = 250)
    city = models.CharField(max_length = 250)
    state = models.CharField(max_length = 250)
    zipcode=models.IntegerField(default = 00000)

    def __str__(self):
        """Return a string representation of the model."""
        return self.address

class Lease(models.Model):
    #Leasing information for company's facilities
    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    text = models.CharField('Leasee', default = 'Leasee', max_length = 150)
    rate = models.FloatField(default = 0.00)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    date = models.DateField('Start Date')

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Soft_Service(models.Model):
    #soft facility serives include items not related to physical facility
    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    text = models.CharField('Soft_Service', default = 'Soft_Service', max_length = 250)
    security_crew_title = models.CharField(max_length = 200)
    cleaning_crew_title = models.CharField(max_length = 200)
    landscaping_crew_title = models.CharField(max_length = 200)
    caterer = models.CharField(max_length = 200)

    def __str__(self):
        """Return a string represntation of the model."""
        return self.text
    
class Safety_Service(models.Model):
    #Safety services include items such as first aid training
    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    text = models.CharField('Safety_Service', default = 'Safety_Service', max_length = 250)
    training_schedule = models.DateTimeField('training schedule')
    audit_schedule = models.DateTimeField('audit schedule')
    safety_meetings = models.DateTimeField ('meeting schedule')
    safety_coordinator = models.CharField(max_length = 150)
    job_safety_analysis = models.CharField (max_length = 500)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Hard_Service(models.Model): 
    #Hard services include overhead services such as utilities
    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    text = models.CharField('Hard_Service', default = 'Hard_Service', max_length = 250)
    electric_provider = models.CharField(max_length = 200)
    plumbing_provider = models.CharField(max_length = 200)
    hvac_provider = models.CharField(max_length = 200)
    mechanical_provider = models.CharField(max_length = 200)
    fire_safety_provider = models.CharField(max_length = 200)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.text
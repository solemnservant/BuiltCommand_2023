from django.contrib import admin

# Register your models here.
from .models import Member, Safety_Service, Soft_Service, Hard_Service, Location, Lease

admin.site.register(Member)
admin.site.register(Location)
admin.site.register(Lease)
admin.site.register(Safety_Service)
admin.site.register(Soft_Service)
admin.site.register(Hard_Service)
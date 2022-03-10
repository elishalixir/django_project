from django.contrib import admin
from .models import userdata
#from django.contrib.auth.models import Group



# Register your models here.
admin.site.site_header='Mercury MIS'
admin.site.register(userdata)
#admin.site.unregister(Group)

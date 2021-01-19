from django.contrib import admin

# Register your models here.
from .models import Growth,Farm,Manage
admin.site.register(Farm)
admin.site.register(Manage)
admin.site.register(Growth)

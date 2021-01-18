from django.contrib import admin

# Register your models here.
from .models import Growth,Environment,Farm,Manage
admin.site.register(Farm)
admin.site.register(Manage)
admin.site.register(Growth)
admin.site.register(Environment)

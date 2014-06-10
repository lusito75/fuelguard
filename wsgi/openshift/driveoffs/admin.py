from django.contrib import admin

# Register your models here.
from .models import Driveoff

class DriveoffAdmin(admin.ModelAdmin):
    class Meta:
        model = Driveoff

admin.site.register(Driveoff, DriveoffAdmin)

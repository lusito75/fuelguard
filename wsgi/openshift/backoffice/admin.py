from django.contrib import admin

# Register your models here.
from .models import CustomerProfile

class CustomerProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = CustomerProfile

admin.site.register(CustomerProfile, CustomerProfileAdmin)

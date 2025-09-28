from django.contrib import admin
from base.models import Person

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "age", "details")
admin.site.register(Person, PersonAdmin)
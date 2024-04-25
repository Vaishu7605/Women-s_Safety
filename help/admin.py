from django.contrib import admin
from .models import *

@admin.register(clients)
class clients(admin.ModelAdmin):
    list_display = ('First_Name', 'Last_Name','E_mail','Create_Password',)


admin.site.register(Feedback)



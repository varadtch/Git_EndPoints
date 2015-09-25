from django.contrib import admin
from models import Userdatabase

class UserdatabaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'profession')
admin.site.register(Userdatabase, UserdatabaseAdmin)

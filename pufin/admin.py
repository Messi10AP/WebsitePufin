from django.contrib import admin
from .models import UserInfo

class UserAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name']
    list_display = ['first_name','last_name']

    def first_name(self,obj):
        return obj.user.first_name

    def last_name(self,obj):
        return obj.user.last_name

admin.site.register(UserInfo, UserAdmin)

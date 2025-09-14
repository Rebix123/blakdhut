from django.contrib import admin
from user.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'full_name',]
    search_fields = ['username', 'email', 'full_name']


admin.site.register(User, UserAdmin)


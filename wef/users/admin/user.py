from django.contrib import admin

from users.models import User


class UserModelAdmin(admin.ModelAdmin):

        list_display = admin.ModelAdmin.list_display + (
            'phone',
            'email',
            )

admin.site.register(User, UserModelAdmin)

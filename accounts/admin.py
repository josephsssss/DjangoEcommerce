from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from accounts.models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email', 'name', 'username', 'gender', 'date_joined', 'last_login', 'is_active')
    list_display_links = ('email', 'username')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)

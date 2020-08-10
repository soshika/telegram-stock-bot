from django.contrib import admin
from .models import Account

# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    fields = ['firstName', 'lastName', 'username', 'status', 'commission']
    list_display = ['id', 'firstName', 'lastName', 'username', 'status', 'commission']
    search_fields = ['firstName', 'lastName', 'username']
    list_filter = ['status']
    list_per_page = 10


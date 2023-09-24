from django.contrib import admin
from .models import Status
# Register your models here.

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = (
                    'access',
                    'data_type',
                    'param_index',
                    'param_sub_index',
                    'error_returned',
                    'transfer_value',
                    'timestamp'
                    )

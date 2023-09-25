from django.contrib import admin
from .models import Status, VaemState
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

@admin.register(VaemState)
class VaemStatusViewAdmin(admin.ModelAdmin):
    list_display = (
                    'status',
                    'error',
                    'readiness',
                    'operating_mode',
                    'valve1',
                    'valve2',
                    'valve3',
                    'valve4',
                    'valve5',
                    'valve6',
                    'valve7',
                    'valve8',
                    'timestamp'
                    )

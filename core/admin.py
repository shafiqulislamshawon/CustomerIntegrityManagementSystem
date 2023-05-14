from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from core.models import *


# Register your models here.

class TransactionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(TransactionCount)

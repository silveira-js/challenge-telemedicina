from django.contrib import admin

from core.models import Examination, Patient, ExamType, Doctor

class ExaminationAdmin(admin.ModelAdmin):
    list_filter = ('altered',)
    readonly_fields = ["altered"]
    list_display = ["id"]

admin.site.register(Examination, ExaminationAdmin)
admin.site.register(Patient)
admin.site.register(ExamType)
admin.site.register(Doctor)
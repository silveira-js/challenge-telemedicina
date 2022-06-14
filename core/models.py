from django.core.exceptions import ValidationError
from django.db import models
from core.utils import format_text_report
import core.definitions as definitions


class ExamType(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=16)

    def __str__(self) -> str:
        return f"{self.code} - {self.name}"

class Patient(models.Model):
    FEMALE = 'F'
    MALE = 'M'
    SEX_CHOICES = [(FEMALE, 'Female'), (MALE, 'Male')]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Doctor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    crm_number = models.IntegerField()
    speciality = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Examination(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    exam_type = models.ForeignKey(ExamType, on_delete=models.PROTECT) 
    report = models.TextField()
    altered = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f"{self.patient} - {self.exam_type}"

    def clean(self):
        formatted_report = format_text_report(self.report)
        if formatted_report not in (definitions.ALTERED_STATUS + definitions.NOT_ALTERED_STATUS):
            raise ValidationError('This report is not valid!')
        return super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        formatted_report = format_text_report(self.report)
        if formatted_report in definitions.ALTERED_STATUS:
            self.altered = True
        elif formatted_report in definitions.NOT_ALTERED_STATUS:
            self.altered = False
        super(Examination, self).save(*args, **kwargs)


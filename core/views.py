from telnetlib import DO
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins

from rest_framework.permissions import IsAuthenticated

from core.filters import ExaminationFilterSet
from core.serializers import DoctorSerializer, ExamTypeSerializer, ExaminationSerializer, PatientSerializer
from core.models import Examination, ExamType, Patient, Doctor


class ExaminationView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ExaminationSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = ExaminationFilterSet
    
    def get_queryset(self):
        queryset = Examination.objects.all().select_related('patient', 'doctor', 'exam_type')
        return queryset


class ExamTypeView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ExamTypeSerializer

    def get_queryset(self):
        queryset = ExamType.objects.all()
        return queryset


class PatientView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PatientSerializer

    def get_queryset(self):
        queryset = Patient.objects.all()
        return queryset


class DoctorView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = DoctorSerializer

    def get_queryset(self):
        queryset = Doctor.objects.all()
        return queryset
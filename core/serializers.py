from rest_framework import serializers
from core.models import Doctor, ExamType, Examination, Patient


class ExamTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExamType
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = '__all__'


class ExaminationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Examination
        fields = [
            'patient', 
            'doctor', 
            'exam_type',
            'report', 
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['altered'] = instance.altered
        data['patient'] = PatientSerializer(instance.patient).data
        data['doctor'] = DoctorSerializer(instance.doctor).data
        data['exam_type'] = ExamTypeSerializer(instance.exam_type).data
        return data
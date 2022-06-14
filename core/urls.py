from email.mime import base
from nturl2path import url2pathname
from django.urls import path
from rest_framework import routers
from core.models import Patient
from core.views import DoctorView, ExamTypeView, ExaminationView, PatientView
from rest_framework.authtoken.views import obtain_auth_token

router = routers.SimpleRouter()
router.register(r'examinations', ExaminationView, basename="examinations")
router.register(r'exam-types', ExamTypeView, basename="exam-types")
router.register(r'doctors', DoctorView, basename="doctors")
router.register(r'patients', PatientView, basename="patient")

urlpatterns = router.urls + [
    path('token-auth/', obtain_auth_token, name="token-auth")
]

import factory.fuzzy
import datetime
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from core.models import Doctor, ExamType, Examination, Patient

class UserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.Faker('email')
    password = factory.PostGenerationMethodCall(
        'set_password', 'defaultpassword'
    )

    class Meta:
        model = User

class TokenFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Token

class ExamTypeFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('pystr')
    code = factory.Faker('pystr')

    class Meta:
        model = ExamType

class PatientFactory(factory.django.DjangoModelFactory):
    sex = factory.fuzzy.FuzzyChoice(
        Patient.SEX_CHOICES, getter=lambda c: c[0]
    )
    first_name = factory.Faker('pystr')
    last_name = factory.Faker('pystr')
    birth_date = factory.fuzzy.FuzzyDate(
        start_date=datetime.date(1, 1, 1)
    )
    address = factory.Faker('pystr')
    phone = factory.Faker('pystr')

    class Meta:
        model = Patient

class DoctorFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('pystr')
    last_name = factory.Faker('pystr')
    crm_number = factory.Faker('pyint')
    speciality = factory.Faker('pystr')

    class Meta:
        model = Doctor

class ExaminationFactory(factory.django.DjangoModelFactory):
    patient = factory.SubFactory(PatientFactory)
    doctor = factory.SubFactory(DoctorFactory)
    exam_type = factory.SubFactory(ExamTypeFactory)
    report = factory.Faker('text', max_nb_chars=2000)

    class Meta:
        model = Examination
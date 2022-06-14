import datetime
from django.core.management.base import BaseCommand
from core.factories import DoctorFactory, PatientFactory, ExamTypeFactory, ExaminationFactory

class Command(BaseCommand):
    help = "A command to add data from dataframe"

    def handle(self, *args, **options):
        print('Start Seeding...')

        patient_1 = PatientFactory(
            sex = 'F',
            first_name = 'Emilia',
            last_name = 'Lane',
            birth_date = datetime.date(1990, 5, 22),
            address = 'Avenue Bloomingdale, 67',
            phone = '+1 205-279-7447'
        )
        patient_2 = PatientFactory(
            sex = 'M',
            first_name = 'John',
            last_name = 'Theriot',
            birth_date = datetime.date(1983, 5, 19),
            address = '2247 Farnum Road New York, NY 10007',
            phone = '+1 212-384-6309'
        )
        patient_3 = PatientFactory(
            sex = 'F',
            first_name = 'Susan',
            last_name = 'Edmunds',
            birth_date = datetime.date(1980, 1, 31),
            address = '46 Poplar Chase Lane Arbon, ID 83212',
            phone = '+1 Susan F. Edmunds'
        )

        doctor_1 = DoctorFactory(
            first_name = 'Joao', 
            last_name = 'Gomez',
            crm_number = 121431,
            speciality = 'Ginecologista'
        )
        doctor_2 = DoctorFactory(
            first_name = 'Pedro', 
            last_name = 'Soares',
            crm_number = 421322,
            speciality = 'Pediatra'
        )
        doctor_3 = DoctorFactory(
            first_name = 'Felipe', 
            last_name = 'Machado',
            crm_number = 321431,
            speciality = 'Neurologista'
        )

        exam_type_1 = ExamTypeFactory(
            name = "Ácido Homogentísico",
            code = "AHO"
        )
        exam_type_2 = ExamTypeFactory(
            name = "Glicose",
            code = "GLI"
        )
        exam_type_3 = ExamTypeFactory(
            name = "Colesterol",
            code = "COL"
        )

        examination_1 = ExaminationFactory(
            doctor=doctor_1,
            patient=patient_1,
            report="o exame não esta normal",
            exam_type=exam_type_1
        )
        examination_2 = ExaminationFactory(
            doctor=doctor_2,
            patient=patient_1,
            report="exame normal",
            exam_type=exam_type_2
        )
        examination_3 = ExaminationFactory(
            doctor=doctor_3,
            patient=patient_2,
            report="exame alterado",
            exam_type=exam_type_3
        )
from curses.ascii import alt
from pydoc import resolve
from urllib import response
from django.urls import reverse
import datetime
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from core.factories import ExamTypeFactory, ExaminationFactory, TokenFactory, UserFactory, PatientFactory, DoctorFactory
from core.models import ExamType
from core.test_utils import build_url_with_query_params

class ExaminationViewTestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_it_generates_token(self):
        token = TokenFactory(user=self.user)
        saved_token = Token.objects.get(user=self.user)
        self.assertEqual(token, saved_token)

    def test_it_requires_authentication(self):
        response = self.client.get(reverse('examinations-list'))
        self.assertEqual(response.status_code, 401)

    def test_it_authenticates(self):
        token = TokenFactory(user=self.user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get(reverse('examinations-list'))
        self.assertEqual(response.status_code, 200)

    def test_it_returns_altered_true_when_report_is_not_normal(self):
        altered_examination_1 = ExaminationFactory(
            report='o exame esta alterado.'
        )
        altered_examination_2 = ExaminationFactory(
            report='o exame não esta normal'
        )
        altered_examination_3 = ExaminationFactory(
            report='exame nao normal'
        )
        altered_examination_4 = ExaminationFactory(
            report='exame alterado'
        )

        self.assertEqual(altered_examination_1.altered, True)
        self.assertEqual(altered_examination_2.altered, True)
        self.assertEqual(altered_examination_3.altered, True)
        self.assertEqual(altered_examination_4.altered, True)
        
    def test_it_returns_altered_false_when_report_is_normal(self):
        not_altered_examination_1 = ExaminationFactory(
            report='O Exame está normal'
        )
        not_altered_examination_2 = ExaminationFactory(
            report='exame normal'
        )
        not_altered_examination_3 = ExaminationFactory(
            report='conclusão: normal'
        )

        self.assertEqual(not_altered_examination_1.altered, False)
        self.assertEqual(not_altered_examination_2.altered, False)
        self.assertEqual(not_altered_examination_3.altered, False)

    def test_it_returns_only_altered_examinations(self):
        altered_examination_1 = ExaminationFactory(
            report='o exame esta alterado.'
        )
        altered_examination_2 = ExaminationFactory(
            report='o exame não esta normal'
        )
        altered_examination_3 = ExaminationFactory(
            report='exame nao normal'
        )
        altered_examination_4 = ExaminationFactory(
            report='exame alterado'
        )

        not_altered_examination_1 = ExaminationFactory(
            report='O Exame está normal'
        )
        not_altered_examination_2 = ExaminationFactory(
            report='o exame não está alterado'
        )

        self.client.force_authenticate(user=self.user)
        query_params = {'altered': True}
        url = build_url_with_query_params('examinations-list', query_params)
        
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.data[0]['altered'], altered_examination_1.altered)
        self.assertEqual(response.data[1]['altered'], altered_examination_2.altered)
        self.assertEqual(response.data[2]['altered'], altered_examination_3.altered)
        self.assertEqual(response.data[3]['altered'], altered_examination_4.altered)

    def test_it_returns_only_not_altered_examinations(self):
        altered_examination_1 = ExaminationFactory(
            report='o exame esta alterado.'
        )
        altered_examination_2 = ExaminationFactory(
            report='o exame não esta normal'
        )
        not_altered_examination_1 = ExaminationFactory(
            report='O Exame está normal'
        )
        not_altered_examination_2 = ExaminationFactory(
            report='exame normal'
        )
        not_altered_examination_3 = ExaminationFactory(
            report='conclusão: normal'
        )

        self.client.force_authenticate(user=self.user)
        query_params = {'altered': False}
        url = build_url_with_query_params('examinations-list', query_params)
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['altered'], not_altered_examination_1.altered)
        self.assertEqual(response.data[1]['altered'], not_altered_examination_2.altered)
        self.assertEqual(response.data[2]['altered'], not_altered_examination_3.altered)

    def test_if_can_edit_examination(self):
        self.client.force_authenticate(user=self.user)
        altered_examination = ExaminationFactory(
            report='o exame esta alterado.'
        )
        response_1 = self.client.get(reverse('examinations-detail', kwargs={'pk': altered_examination.id}))
        self.assertEqual(response_1.data['altered'], True)

        payload_2 = {
            'patient' : altered_examination.patient.id,
            'doctor' : altered_examination.doctor.id,
            'exam_type' : altered_examination.exam_type.id,
            'report' : 'O exame esta normal'
        }
        response_2 = self.client.put(reverse('examinations-detail', kwargs={'pk': altered_examination.id}), data=payload_2)
        
        self.assertEqual(response_2.status_code, 200)
        self.assertEqual(response_2.data['altered'], False)

    def test_if_can_delete_examination(self):
        self.client.force_authenticate(user=self.user)
        altered_examination = ExaminationFactory(
            report='o exame esta alterado.'
        )
        response = self.client.delete(reverse('examinations-detail', kwargs={'pk': altered_examination.id}))
        self.assertEqual(response.status_code, 204)

    def test_it_requires_only_one_query_from_db(self):
        examination = ExaminationFactory(
            report='O exame esta normal'
        )
        self.client.force_authenticate(user=self.user)
        with self.assertNumQueries(1):
            response_1 = self.client.get(reverse('examinations-detail', kwargs={'pk': examination.id}))
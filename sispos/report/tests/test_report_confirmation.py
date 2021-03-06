from django.test import TestCase
from django.shortcuts import resolve_url as r
from unittest import mock
from django.core.files import File
from sispos.report.models import Report, Semestre
from sispos.accounts.models import User


class ReportConfirmationTest(TestCase):
    def setUp(self):
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'test.pdf'
        
        aluno = User.objects.create_user(
            login='3544444',
            main_email='main@test.com',
            password='92874',
            name='Marc',
            type='I'
        )

        report = Report.objects.create(aluno=aluno)
        
        Semestre.objects.create(
            semestre='Primeiro Semestre', 
            relator='Relator 1', 
            orientador='Orientador 1',
            programa='Mestrado',
            relatorio=file_mock,
            encaminhamento=file_mock,
            report=report
        )

        self.resp = self.client.get(r('report:confirmation', slug=report.uuid))

    def test_confirmation(self):
        """Must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must render report_confirmation.html"""
        self.assertTemplateUsed(self.resp, 'report_confirmation.html')

    def test_inherite_main_template(self):
        """It should inherite main.html template"""
        self.assertTemplateUsed(self.resp, 'main.html')

    def test_page_title(self):
        """Page must contain its title"""
        self.assertContains(self.resp, 'Confirmação de envio')

    def test_html(self):
        contents = [
            'Orientador 1',
            'Mestrado',
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected)


        
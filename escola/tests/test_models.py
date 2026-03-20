from django.test import TestCase
from escola.models import Estudante,Curso,Matricula
from django.db.utils import IntegrityError

class ModelEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'testedemodelo@gmail.com',
            cpf='17097057017',
            data_nascimento = '2026-03-20',
            celular = '86 99999-9999'
        )
    
    def test_verifica_atributos_de_estudante(self):
        '''Teste que verifica os atributos do modelo de Estudante'''
        self.assertEqual(self.estudante.nome,'Teste de Modelo')
        self.assertEqual(self.estudante.email,'testedemodelo@gmail.com')
        self.assertEqual(self.estudante.cpf,'17097057017')
        self.assertEqual(self.estudante.data_nascimento,'2026-03-20')
        self.assertEqual(self.estudante.celular,'86 99999-9999')

    def test_verifica_restricao_de_unicidade_de_cpf(self):
        '''Teste que verifica a restrição UNIQUE do campo de CPF'''
        Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'testedemodelo@gmail.com',
            cpf='07794078067',
            data_nascimento = '2026-03-20',
            celular = '86 99999-9999'
        )
        with self.assertRaises(IntegrityError) as error:
            Estudante.objects.create(
                nome = 'Teste de Modelo',
                email = 'testedemodelo@gmail.com',
                cpf='07794078067',
                data_nascimento = '2026-03-20',
                celular = '86 99999-9999'
            )

        self.assertTrue(isinstance(error.exception, IntegrityError))

class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo='PO1',
            descricao='Descrição do curso de teste',
            nivel='B'
        )

    def test_verifica_atributos_de_curso(self):
        '''Teste que verifica os atributos do modelo de Curso'''
        self.assertEqual(self.curso.codigo,'PO1')
        self.assertEqual(self.curso.descricao,'Descrição do curso de teste')
        self.assertEqual(self.curso.nivel,'B')

    def test_verifica_restricao_de_nivel(self):
        '''Teste que verirfica a restrição do enum de Niveis'''
        with self.assertRaises(IntegrityError) as error:
            Curso.objects.create(
                codigo='PO1',
                descricao='Descrição do curso de teste',
                nivel='D'
            )

        self.assertTrue(isinstance(error.exception, IntegrityError))
        self.assertIn('UNIQUE constraint failed: escola_curso.codigo', str(error.exception))

class ModelMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante_matricula = Estudante.objects.create(
            nome = 'Teste Modelo Matricula',
            email='testemodelomatricula@gmail.com',
            cpf='91546870040',
            data_nascimento='2003-02-02',
            celular='86 99999-9999'
        )
        self.curso_matricula = Curso.objects.create(
            codigo='CTMM',descricao='Curso Teste Modelo Matricula',nivel='B'
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante_matricula,
            curso=self.curso_matricula,
            periodo='M'
        )

    def test_verifica_atributos_de_matricula(self):
        '''Teste que verifica os atributos do modelo de Matricula'''
        self.assertEqual(self.matricula.estudante.nome, 'Teste Modelo Matricula')
        self.assertEqual(self.matricula.curso.descricao, 'Curso Teste Modelo Matricula')
        self.assertEqual(self.matricula.periodo, 'M')

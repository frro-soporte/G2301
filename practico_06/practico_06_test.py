# Implementar los casos de prueba descriptos.

import unittest

from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import NegocioSocio, LongitudInvalida


class TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.ns = NegocioSocio()

    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.ns.datos.borrar_todos()

    def test_alta(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        # post-condiciones: 1 socio registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 1)

    def test_regla_1(self):
        pass

    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        invalido = Socio(dni=12345678, nombre='Juan' * 5, apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))
        invalido = Socio(dni=12345678, nombre='Juan', apellido='P')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Perez' * 5)
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_3(self):
        pass

    def test_baja(self):
        # pre-condiciones: existe un socio registrado
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)
        self.assertEqual(len(self.ns.todos()), 1)

        # ejecuto la lógica
        exito = self.ns.baja(socio.id)

        # post-condiciones: el socio ha sido eliminado
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 0)

    def test_buscar(self):
        # pre-condiciones: existe un socio registrado
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)

        # ejecuto la lógica
        socio_encontrado = self.ns.buscar(socio.id)

        # post-condiciones: el socio ha sido encontrado
        self.assertIsNotNone(socio_encontrado)
        self.assertEqual(socio_encontrado, socio)

    def test_buscar_dni(self):
        # pre-condiciones: existe un socio registrado
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)

        # ejecuto la lógica
        socio_encontrado = self.ns.buscar_dni(socio.dni)

        # post-condiciones: el socio ha sido encontrado
        self.assertIsNotNone(socio_encontrado)
        self.assertEqual(socio_encontrado, socio)

    def test_todos(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # agrego algunos socios
        socios = [
            Socio(dni=12345678, nombre='Juan', apellido='Perez'),
            Socio(dni=98765432, nombre='Carlos', apellido='Gomez'),
            Socio(dni=45678912, nombre='Laura', apellido='Lopez')
        ]
        for socio in socios:
            self.ns.alta(socio)

        # ejecuto la lógica
        socios_encontrados = self.ns.todos()

        # post-condiciones: se han encontrado todos los socios
        self.assertEqual(len(socios_encontrados), len(socios))
        self.assertCountEqual(socios_encontrados, socios)

    def test_modificacion(self):
        # pre-condiciones: existe un socio registrado
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)

        # modifico los datos del socio
        socio.nombre = 'Carlos'
        socio.apellido = 'Gomez'
        socio.dni = 98765432

        # ejecuto la lógica
        socio_modificado = self.ns.modificacion(socio)

        # post-condiciones: el socio ha sido modificado
        self.assertIsNotNone(socio_modificado)
        self.assertEqual(socio_modificado.id, socio.id)
        self.assertEqual(socio_modificado.nombre, 'Carlos')
        self.assertEqual(socio_modificado.apellido, 'Gomez')
        self.assertEqual(socio_modificado.dni, 98765432)

from src.Zadanie2.Car import Car
from unittest.mock import *
from unittest import TestCase, main


class TestCarPublicInterface(TestCase):
    def test_needsFuel(self):
        # prepare mock
        test_object = Car()
        test_object.needsFuel = Mock(name='needsFuel')
        test_object.needsFuel.return_value = False

        # testing
        result = test_object.needsFuel()
        self.assertEqual(False, result, 'return value from needsFuel incorrect')

    def test_getEngineTemperature(self):
        # prepare mock
        test_object = Car()
        test_object.getEngineTemperature = Mock(name='getEngineTemperature')
        test_object.getEngineTemperature.return_value = 100

        # testing
        result = test_object.getEngineTemperature()
        self.assertEqual(100, result, 'return value from getEngineTemperature incorrect')

    def test_driveTo(self):
        # prepare mock
        test_object = Car()
        test_object.driveTo = Mock(name='driveTo')
        destination = "Bieszczady"
        test_object.driveTo.return_value = f'Destination: {destination}'

        # testing
        result = test_object.driveTo('Bieszczady')
        self.assertEqual('Destination: Bieszczady', result, 'return value from driveTo incorrect')


if __name__ == '__main__':
    main()
from src.Zadanie3.Checker import Checker
from unittest.mock import *
from unittest import TestCase, main


class TestCarPublicInterface(TestCase):
    def test_getTime(self):
        # prepare mock
        test_object = Checker()
        test_object.alarm_clock.getTime = Mock(name='getTime')
        test_object.alarm_clock.getTime.return_value = 16

        test_object.alarm_clock.wavWasPlayed = Mock(name='wavWasPlayed')
        test_object.alarm_clock.wavWasPlayed.return_value = False

        # testing
        file = "plik.wav"
        result = test_object.alarm_clock.wavWasPlayed(file)
        self.assertEqual(False, result, 'return value incorrect')


if __name__ == '__main__':
    main()
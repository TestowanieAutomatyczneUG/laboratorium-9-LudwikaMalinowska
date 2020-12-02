
from Zadanie3.AlarmClock import AlarmClock

class Checker:

    def __init__(self):
        self.alarm_clock = AlarmClock()

    def remainder(self, file):
        hour = self.alarm_clock.getTime()
        if hour > 17:
            self.alarm_clock.playWavFile(file)
            self.alarm_clock.wavWasPlayed()



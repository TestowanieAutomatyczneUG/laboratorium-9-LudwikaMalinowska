
class AlarmClock:

    wavPlayed = False

    def getTime(self):
        pass

    def playWavFile(self, file):
        pass

    def wavWasPlayed(self, file):
        self.wavPlayed = True

    def resetWav(self):
        self.wavPlayed = False

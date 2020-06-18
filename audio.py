class AudioFile:
    def __init__(self,filename):
        if not filename.endwith(self.ext):
            raise Exception("Invalid file format")

        self.filename = filename

class MP3File(AudioFile):
    ext = "mp3"
    def play(self):
        print("playing mp3")


class WavFile(AudioFile):
    ext = "wav"

    def play(self):
        print("playing wav")


class OggFile(AudioFile):
    ext = "ogg"

    def play(self):
        print("playing ogg")

class FlacFile:
    def __init__(self,filename):
        if not filename.endwith('.flac'):
            raise Exception("Invalid file format")

        self.filename = filename

    def play(self):
        print('print flac')
import threading
from playsound import playsound


class GameSound:
    JUMP_SOUND = 'assets/sound/jump_sound.wav'
    TOKEN_SOUND = 'assets/sound/token_sound.mp3'

    def __init__(self, path):
        self.path = path

    def play_async(self):
        thread = threading.Thread(target=playsound, args=(self.path, ))
        thread.start()
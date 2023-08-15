from playsound import playsound, PlaysoundException
import threading
import multiprocessing

class GameSound:
    TOK_COLLECT = 'assets/sounds/cheese_collect.mp3'
    JUMP_SOUND = 'assets/sounds/jump_sound.wav'

    def __init__(self, filepath):
        self.thread = multiprocessing.Process(target=self.play_asynch, args=(filepath,))

    def play_asynch(self, file):
        playsound(file)

    def play_sound(self):
        self.thread.start()
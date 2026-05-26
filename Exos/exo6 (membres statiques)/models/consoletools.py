import os
import time

class Outils():
    @staticmethod
    def clear_console():
        os.system('cls')

    @staticmethod
    def pause(secondes):
        print(f"\n { "=" * 50} \n Pause de {secondes} secondes")
        time.sleep(secondes)
        


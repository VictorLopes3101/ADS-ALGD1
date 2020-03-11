
from random import randint
from time import sleep

class bottle_falling():

    def main(self):
        bottle_falling = 0
        self.running_belt(bottle_falling)
        pass
    
    def running_belt(self, bottle):
        running = True
        bottle_run = 0
        while running:
            probability = randint(0, 100)
            if probability >= 20:
                bottle_run += 1
                print('Bottle Status: OK')
            else:
                print('Bottle Status: FALL')
                print('Stopping the belt')
                break
            sleep(0.5)
        print(f'The number of bottles passed {bottle_run}')

if __name__ == '__main__':
    run = bottle_falling()
    run.main()

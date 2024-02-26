import keyboard
from time import sleep



def main():


    while True:
        sleep(0.02)

        if keyboard.is_pressed("space"):
            keyboard.press_and_release('space')
            sleep(0.07) 
            continue


if __name__ == '__main__':
    main()
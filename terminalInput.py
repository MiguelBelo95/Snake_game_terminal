import tty
import os, sys
import threading
import datetime
import time
import sys

fileno = sys.stdin.fileno() #What does this do, exactly?
tty.setcbreak(fileno) #No need to press enter for 'run' input, and doesn't print the keys pressed on the screen
running = True #create variable running and assign value 'True'

class TerminalReader:
    def __init__(self): #consctructor of struct/class
        self.running = True #properties of the TerminalReader object
        self.list_keys_pressed = {} # Initialise Dictionary of keys pressed

    def run(self): #creating a Method (function) that belongs to object TerminalReader
       
        while self.running: #while true, keep going infinitely
            try: #Keep trying executing code until error appears
                global key 
                key = sys.stdin.read(1).lower() #saves key that has been pressed, changing it to lowercase if Caps
                key_pressed_time = datetime.datetime.now() #variable to store time in which key has been pressed
                self.list_keys_pressed[key] = key_pressed_time #store the key and its time in the dictionary
            except KeyboardInterrupt: #when error KeyboardInterrupt appears, run 'finish' function
                self.finish()

    def finish(self): #Method of TerminalReader, only called when while function hits KeyboardInterrup (^c)
        self.running = False #function changes self.running to false --> infinite loop finishes
    
    def is_clicking(self, key): #Identifies the key that is currently being pressed
        n_seconds_passed = self.duration_of_key_pressed_in_seconds(key)
        if ( float(n_seconds_passed) < 0.3): #if time when key (eg)'w' was pressed - 'current time now' is > 0,15s
            # then is clicking w is true and should return something?
            return True
        return False #Else return False

    def ever_clicked_on_key(self, key):
        # First
        if (key in self.list_keys_pressed): #search the key value on the dictionary
            return True #if exists, returns True
        else:
            return False #if doesn't exist, returns False

    def duration_of_key_pressed_in_seconds(self, key): #Returns amount of seconds that passed since key was pressed
        # Second
        if (self.ever_clicked_on_key(key)): #if key has indeed been pressed before, then...
            now = datetime.datetime.now() #Exactly time in present moment
            k_pressed_seconds = self.list_keys_pressed.get(key) #get time of key pressed, by acessing Dict key:vaule pair
            n_seconds_passed = abs(now - k_pressed_seconds).total_seconds() #subtract and get the absolute result in seconds
            return n_seconds_passed
        else:
            return 1 #if key has never been clicked before



terminalReader = TerminalReader() #Assign object TerminalReader to variable terminalReader
t = threading.Thread(target=terminalReader.run) #Corre em paralelismo

t.start()

def is_clicking(key): 
    return terminalReader.is_clicking(key)

if __name__ == "__main__": # __name__ means 'Main' that is defined by python, when runned in this program
    while True:
        time.sleep(0.15)
        if (terminalReader.is_clicking('a')):
            print("User is clicking a Key!!!")
        else:
            print("ASDF")
            
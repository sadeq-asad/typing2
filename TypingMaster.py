# 1-Create a class that measures typing speed
from time import time
from random import randint

class TypingSpeed():
    def __init__(self, name):
        self.name = name       
                
    @staticmethod
    def inception():
        asciii = open("ascii.txt", "r").read()
        print(asciii) 
        typist_name = input("Enter your name: ")     
        ready = input("Hello %s. Welcome to Typing Master. Start typing test? " % typist_name).strip()
        if ready.lower() == "yes": 
            print("\n")
            new_test = TypingSpeed(typist_name)
            new_test.measure_speed()
        else:
            print("Goodbye!") 
               
    def measure_accuracy(self, typed, source):
        accurate = 0
        source_words = 0
        z = list(zip(typed, source))
        for x, y in z:
            if x == y:
                accurate += 1
                source_words += 1
            else:
                source_words += 1
        result = "Your accuracy is %s percent" % str((accurate/source_words) * 100)
        return result
        
    def measure_speed(self):
        text = open("Typing.txt", "r").readlines()
        random_text = text[randint(0, len(text)-1)]
        print(random_text)
        time1 = time()
        words_typed = input("Start typing now! \n")
        time2 = time()
        if words_typed:
            words_typed = words_typed.split(" ")
            speed = (len(words_typed)) / ((time2 - time1) / 60)
            print("\nYour speed is %s words per minute\n" % round(speed))
            print(self.measure_accuracy(words_typed, random_text.split()))
            self.another_test()
        else:
            print("You haven't typed any word!")
            self.another_test()
            
    def another_test(self):
        question = input("Start another test? ").strip()
        if question.lower() == "yes":
            self.measure_speed()
        else:
            print("Goodbye!")        

TypingSpeed.inception()
#add accuracy
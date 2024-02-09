import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import tkinter as tk
from tkinter import *
root = Tk()
root.geometry('300x300')
root.title('Mad Libs Generator')
root.config(bg= 'Green')
Label(root, text= 'Mad Libs Generator \n Have Fun!' , font = 'arial 20 bold', bg = 'Green').pack()
Label(root, text = 'Click Any One', font = 'arial 15 bold', bg = 'Green').place(x=80, y=80)
def madlib1():
    Name = input('Enter a Name: ')
    adjective1 = input('Enter a Adjective: ')
    adjective2 = input('Enter another Ajective: ')
    adjective3 = input('One more time, enter a Adjective of your choice: ')
    Noun1 = input('Enter a Thing: ')
    Noun3 = input('Enter a Place: ')
    Noun2 = input('Enter a part of the Face: ')
    Exclamation = input ('Enter a Exclamation like Oops or Dang It:  ')
    print("")
    print('Once upon a time, in a bustling city, there was a pizza delivery person named ' + Name + '.' + Name + ' was known for their ' + adjective1 + ' sense of humor and their love for ' + adjective2 + ' pizza. One day, while delivering a pizza to a ' + adjective3 + ' house,' + Name + ' encountered a ' + adjective1 + ' situation. As ' + Name + ' rang the doorbell, they were greeted by a ' + adjective2 + ' man wearing ' + adjective3 + ' socks and holding a ' + Noun1 + '."I have been waiting for this pizza all day!" exclaimed the man, his ' + Noun2 + ' twitching with excitement.But just as ' + Name + ' handed over the pizza, a ' + adjective2+ ' squirrel dashed by, snatching the pizza box with its ' + adjective3 + ' tail and darting up a nearby ' + Noun3 + '.' + Name + ' and the customer stared in disbelief as the squirrel disappeared into the ' + Noun3+ '. Without missing a beat, ' + Name + ' turned to the customer and said, "' + Exclamation +'! Looks like your pizza is on a ' + Noun2 + ' adventure now. Do not worry, we offer free squirrel delivery too!"The customer burst into ' + adjective2 + ' laughter, tipping ' + Name + ' generously for the ' + adjective1 + ' entertainment. And from that day forward, ' + Name + " was known as the city's most " + adjective2 + ' pizza delivery person, always ready to serve up a side of laughter with every order.')
def madlib2():
    Name = input('Enter a Name: ')
    Verb1 = input('Enter a Verb: ')
    adjective1 = input('Enter adjective like super, high ect: ')
    Place= input('Enter a Place: ') 
    animal = input('Enter a Animal: ')
    adjective2= input('Enter another adjective: ')
    adjective3 = input('Enter one more adjective: ')
    print("")
    print('Once upon a time, in a land far, far away, there was a flying banana named '+ Name + '.' + Name + ' was famous for their ability to ' + Verb1 + ' through the sky with ' + adjective1 + ' speed. One sunny day, while soaring above the ' + Place + ',' + Name + 'encountered a mischievous ' + animal + ' who challenged them to a race. Determined to prove their ' + adjective2 + ' prowess, ' + Name + ' accepted the challenge and zoomed ahead with ' + adjective3 + ' determination. Despite facing ' + adjective2 + ' obstacles along the way, ' + Name + ' emerged victorious, earning the admiration of all who witnessed the wacky race.')
def madlib3():
    Adjective1 = input('Enter a Silly Adjective: ')
    Noun = input('Enter a Noun: ')
    Verb1 = input("Enter a Silly Verb ending in 'ing': ")
    Adverb = input('Enter a Adverb: ')
    Animal1 = input('Enter an Anmial in plural: ')
    Adjective2 = input('Enter a funny Adjective: ')
    Verb2 = input('Enter a Verb in past tense: ')
    Number = input('Enter a Number: ')
    Adjective3 = input('Enter one more Adjective: ')
    Animal2 = input('Enter another Animal: ')
    print("")
    print('Once upon a time, in a ' + Adjective1 + ' land far, far away, there lived a peculiar ' + Noun + ' named Mr. Wiggles. He was always ' + Verb1 + ' ' +  Adverb + ' and causing chaos wherever he went. One day, he decided to take his ' + Animal1 + ' for a walk in the ' + Adjective2 + ' park. Suddenly, he ' + Verb2 + ' over a banana peel and did not just fall once, not twice, but ' + Number + ' times! The whole incident was ' + Adjective3 + ' hilarious that even the nearby ' + Animal2 + " goofycouldn't help but laugh along.")  
Button(root, text= 'The Hilarious Pizza Delivery', font ='arial 15', command= madlib1, bg = 'red').place(x=25, y=120)
Button(root, text= 'Saga of the Flying Banana', font ='arial 15', command = madlib2 , bg = 'yellow').place(x=30, y=180)
Button(root, text= 'Misadventures of Mr Wiggles', font ='arial 15', command = madlib3, bg = 'ghost white').place(x=17, y=240)
root.mainloop()

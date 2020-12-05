# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 23:13:38 2020

@author: DELL
"""

from nltk.chat.util import Chat, reflections
pairs=[
       [
        'my name is (.*)',['hi %1']
        ],
       [
        'hi|heya|hola|hey there|heyyaaa|hello',['hello, this is a chatbot.']
        ],
       [
        '(.*) in (.*) is super fun',['Yes, you are right, %1 in %2 is fun.']
        ],
       [
        '(.*)(location|city) ?',['Hapur|India']],
       [
        '(.*) created you ?',['Shivangi did using NLTK']
        ],
       [
        '(.*) weather in (.*) ?',['the weather in %2 is pretty nice']
        ],
       [
        '(.*)help(.*)',['I am here to help!!']
        ],
       [
        '(.*) your name ?',['My name is CHITTHI']
        ],
       ['(.*)quit',['Have a nice day.']]
      ]
dummy_ref={'go':'gone','hello':'hey there'}
chat=Chat(pairs,reflections)
#chat._substitute('you are amazing')
print("Enter quit to exit the program")
chat.converse()


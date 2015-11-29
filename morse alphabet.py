#!/usr/bin/python
# -*- coding: utf8 -*-
########### 
MorseAlphabet = { '1': '.----',	'2': '..---',	'3': '...--',	'4': '....-',	'5': '.....',	'6': '-....',	'7': '--...',	'8': '---..',	'9': '----.',	'0': '-----'}					  ##assigning the morse values 0-9
x=raw_input("Give me the value: ")
def MorseChanging(a):
	for value in a:						  ##detecting the parts of given values 
		print MorseAlphabet[value]##printing the value parts from assigned diction
MorseChanging(x)

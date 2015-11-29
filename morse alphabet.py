#!/usr/bin/python
# -*- coding: utf8 -*-
###########
MorseAlphabet=['.----','..---','...--','....-','.....','-....','--...','---..','----.','-----']####	assigning the morse values 0-9
x=raw_input("Give me the value: ")
def MorseChanging(a):
	if(a<10):
		print MorseAlphabet[a]
		

MorseChanging(x)

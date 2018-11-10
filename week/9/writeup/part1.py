#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("../probable-v2-top1575.txt", 'r')
hashes = open("../hashes", 'r')
w = wordlist.readlines()

# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

for h in hashes: #going through the hashes 
	print(h)
	for line in w: # Going through the wordlist
		for salt in salts: # to prepend to passwords
			password = salt+line.strip('\n') #Prepending onto 
			encrypt = hashlib.sha512(password) #encrypting
			if (encrypt.hexdigest() == h.strip('\n')):
				print("Found a match for") 
				print(password)
				print(h)

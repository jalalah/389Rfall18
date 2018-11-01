#!/usr/bin/env python2

import sys
import struct


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")

print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))

offset = 8 #Starting at 8 because magic and version were already parsed

timestamp, deadValue = struct.unpack("<LL", data[offset:offset+8])

print("TIMESTAMP: %d" % int(timestamp))

offset = 12 # 12 now because the timestamp was 4 bytes

author,deadValue = struct.unpack("<LL", data[offset:offset+8])
print("AUTHOR: %s" % str (author))

offset = 20 # 20 because author was 8 bytes

sectionCount, deadValue = struct.unpack("<LL", data[offset:offset+8])
print("SECTION COUNT: %d" % int(sectionCount))

print("-------  BODY  -------")

offset = 24 # 24 because that is where the header ends

x = 1

# Going through all the sections

while (x <=11):
	
 	# When offset = 247093, an error occurs
	sType,sLen = struct.unpack("<LL", data[offset:offset+8])
	print("\nSECTION TYPE: %d"%int(sType))
	print("SECTION LEN: %d" %int(sLen))
	
	# switch statements here that check what kind of section it is

	# png
	if (sType == 1):
		# 89 50 4E 47 0D 0A 1A 0A
		png, = struct.unpack("<%ds" %sLen, data[offset:offset+sLen])
		pngMagic = "89 50 4E 47 0D 0A 1A 0A" + str(png)
		
	# Array of dwords
	if (sType == 2):

		amountOfWords = sLen/8
		dwordOffset = offset
		print("Amount of words %s" %int(amountOfWords))

		while (amountOfWords >= 0): 
			dword1,dword2 = struct.unpack("<LL", data[dwordOffset:dwordOffset+(8)])
			print(str(dword1), str(dword2))
			amountOfWords = amountOfWords - 1
			dwordOffset = dwordOffset + 8

	# UTF-8-enconded text
	if (sType == 3):
		UTF, = struct.unpack("<%ds" %sLen, data[offset:offset+sLen])
		print(str(UTF))

	# Array of doubles
	if (sType == 4):
		print("hi")	
	# Array of words
	if (sType == 5):
		amountOfWords = (sLen / 4)
		wordOffset = offset
		print("Amount of words %d" %int(amountOfWords))

		while (amountOfWords >= 0): 
			word1,word2 = struct.unpack("<LL", data[wordOffset:wordOffset+(8)])
			print(str(word1), str(word2))
			amountOfWords = amountOfWords - 2
			wordOffset = wordOffset + 8


	# (lat, long) tuple of doubles
	if (sType == 6):
		amountOfWords = (sLen / 4)
		wordOffset = offset
		print("Amount of words %d" %int(amountOfWords))

		while (amountOfWords >= 0): 
			word1,word2 = struct.unpack("<LL", data[wordOffset:wordOffset+(8)])
			print(str(word1), str(word2))
			amountOfWords = amountOfWords - 2
			wordOffset = wordOffset + 8

	# Index of another section
	if (sType == 7):
		print("hi")

	# asci value
	if (sType == 9):
		asci, = struct.unpack("<%ds" %sLen, data[offset:offset+sLen])
		print(str(asci))

	x = x+1
	offset = offset + (sLen + 8) 
	










# hi

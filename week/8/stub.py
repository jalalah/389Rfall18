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

# Going through all the sections

while (offset < len(data)):
	
	sType,sLen = struct.unpack("<LL", data[offset:offset+8])
	print("\nSECTION TYPE: %d"%int(sType))
	print("SECTION LEN: %d" %int(sLen))
	
	# switch statements here that check what kind of section it is

	# png NOT DONE
	if (sType == 1):
		# 89 50 4E 47 0D 0A 1A 0A <-- Magic pbytes for png
		png, = struct.unpack("<%ds" %sLen, data[offset:offset+sLen])
		pngMagic = "89 50 4E 47 0D 0A 1A 0A "
		#print(hex(png))
		file = open("hmrk8", "w")
		file.write(pngMagic + str(png))
		file.close()
		
	# Array of dwords. dwords are 8 bytes
	if (sType == 2):
		dWords = sLen/8  #Amount of dwords there are
		dOffset = offset
		print("Amount of dwords %s" %int(dWords))

		while (dWords > 0): 
			# This one makes me have a second argument for my tuple
			# Even tho a dword is supposed to take all 8 bytes
			dword1, deadVal = struct.unpack("<LL", data[dOffset:dOffset+8])
			print(str(dword1))
			dWords = dWords - 1
			dOffset = dOffset + 8

	# UTF-8-enconded text
	if (sType == 3):
		UTF, = struct.unpack("<%ds" %sLen, data[offset:offset+sLen])
		print(str(UTF))

	# Array of doubles. doubles are 8 bytes
	if (sType == 4):
		doubles = (sLen / 8) # Amount of doubles
		dOffset = offset
		print("Amount of doubles %d" %int(doubles))

		while (doubles > 0): 
			double1, = struct.unpack("<LL", data[dOffset:dOffset+8])
			print(str(double1))
			doubles = doubles - 1
			dOffset = dOffset + 8
	
	# Array of words. words are 4 bytes
	if (sType == 5):
		words = (sLen / 4)
		wOffset = offset
		print("Amount of words %d" %int(words))

		while (words > 0): 
			word1, deadVal = struct.unpack("<LL", data[wOffset:wOffset+8])
			print(str(word1))
			words = words - 1
			wOffset = wOffset + 4

	# (lat, long) tuple of doubles. 
	if (sType == 6):
		dOffset = offset
		double1, deadVal1 = struct.unpack("<LL", data[dOffset:dOffset+8])
		dOffset = dOffset + 8
		double2, deadVal2 = struct.unpack("<LL", data[dOffset:dOffset+8])
		print(str(double1), str(double2))
		
	# Index of another section
	if (sType == 7):
		word, deadValue = struct.unpack("<LL", data[offset: offset+8])
		print(str(word))

	# asci value
	if (sType == 9):
		asci, = struct.unpack("<%ds" %sLen, data[offset:offset+sLen])
		print(str(asci))

	offset = offset + (sLen + 8) 
	

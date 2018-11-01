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

author, deadValue = struct.unpack("<LL", data[offset:offset+8])
print("AUTHOR: %s" % str (author))

offset = 20 # 20 because author was 8 bytes

sectionCount, deadValue = struct.unpack("<LL", data[offset:offset+8])
print("SECTION COUNT: %d" % int(sectionCount))

print("-------  BODY  -------")

offset = 24 # 24 because that is where the header ends

x = 1

# Going through all the sections

while (x <= 11):
	sType,sLen = struct.unpack("<LL", data[offset:offset+8])
	print("\nSECTION TYPE: %d"%int(sType))
	print("SECTION LEN: %d" %int(sLen))
	
	# switch statements here that check what kind of section it is

	if (sType == 1):
		print ("Png\n")

	if (sType == 2):
		print ("array of dwords\n")

	if (sType == 3):
		print ("UTF-8-encoded text\n")

	if (sType == 4):
		print ("array of doubles\n")

	if (sType == 5):
		print ("array of words\n")

	if (sType == 6):
		print ("(lat, long) tuple of doubles\n")

	if (sType == 7):
		print ("index of another section\n")

	if (sType == 9):
		print ("asci\n")

	x = x+1
	offset = offset + (sLen + 8) 
	










# hi

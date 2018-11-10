#CMSC389R-{H4sh-5l!ngInG-h@sH3r}

#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib

host = "142.93.117.193"   # IP address or URL
port = 7331   # port

def return_password(index,data):
	substring = data[index:] # getting the string starting from the hash algo
	subarray = substring.split(' ') #splitting the string
	return subarray[3] #what needs to be hashed
	

sha512 = 'sha512'
sha1 = 'sha1'
sha384 = 'sha384'
sha224 = 'sha224'
sha256 = 'sha256'
md5 = 'md5'

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

x=11

while (x > 0):
	# receive some data
	data = s.recv(1024)
	print(data)

	if sha512 in data:
		print("Found a sha512 match")
		index = data.find(sha512)
		encrypt = hashlib.sha512((return_password(index,data)).strip('>\n'))
		s.send(encrypt.hexdigest())
		s.send("\n")

	elif sha1 in data:
		print("Found a sha1 match")
		index = data.find(sha1)
		encrypt = hashlib.sha1((return_password(index,data)).strip('>\n'))
		s.send(encrypt.hexdigest())
		s.send("\n")

	elif sha384 in data:
		print("Found a sha1 match")
		index = data.find(sha384)
		encrypt = hashlib.sha384((return_password(index,data)).strip('>\n'))
		s.send(encrypt.hexdigest())
		s.send("\n")

	elif sha224 in data:
		print("Found a sha1 match")
		index = data.find(sha224)
		encrypt = hashlib.sha224((return_password(index,data)).strip('>\n'))
		s.send(encrypt.hexdigest())
		s.send("\n")

	elif sha256 in data:
		print("Found a sha1 match")
		index = data.find(sha256)
		encrypt = hashlib.sha256((return_password(index,data)).strip('>\n'))
		s.send(encrypt.hexdigest())
		s.send("\n")

	elif md5 in data:
		print("Found a md5 match")
		index = data.find(md5)
		encrypt = hashlib.md5((return_password(index,data)).strip('>\n'))
		s.send(encrypt.hexdigest())
		s.send("\n")

	x = x-1

# close the connection
s.close()

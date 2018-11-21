#!/usr/bin/env python2
# from the git repo
import socket
import md5py
import struct

host = "142.93.118.186"   # IP address 
port = 1234   # port

# Creating the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

#####################################
### STEP 1: Calculate forged hash ###
#####################################

message = 'Hello'    # original message here

# Recieving the hash of the secret + message 
data = s.recv(1024)
print(data)
s.send("1\n")
data = s.recv(1024)
print(data)
s.send(message+'\n')
data = s.recv(1024)
print(data)

legit = data[39:].strip("\n")     # a legit hash of secret + message goes here, obtained from signing a message

print("HERE IS THE LEGIT HASH")
print(legit)

# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))

malicious = 'malicious'  # put your malicious message here

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()

print("HERE IS THE FAKE HASH")
print(fake_hash)


#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is <redacted> bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a byte with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits

# Secret length is between 6 and 15 bytes

sLen = 6 # starting length at 6

while sLen <= 15:
	count = 1 # Counter to put the appropriate amount of x00 onto padding
	mLen = len(message) + sLen # Length of the message plus the secret length
	padding = "\x80" #Padding always begins with this
	pLen = 56 - mLen # Length of the padding 
			 #(Solved len(secret + message + padding) - 8 bytes = 56 bytes
	
	while count < pLen:
		padding = padding + "\x00"
		count = count + 1

# payload is the message that corresponds to the hash in `fake_hash`
# server will calculate md5(secret + payload)
#                     = md5(secret + message + padding + malicious)
#                     = fake_hash
	bitAmount = mLen * 8 # Was working in bytes so have to convert to bits
	padding += struct.pack("<q", bitAmount)

	payload = message + padding + malicious

	s.send("2\n") # Choosing option 2
	data = s.recv(1024)
	print(data.strip())
	s.send(fake_hash+'\n') #Sending the fake hash
	data = s.recv(1024)
	print(data.strip())
	s.send(payload+'\n') #Sending payload
	data = s.recv(1024)
	print(data.strip())

	sLen = sLen + 1 #Increase the length of the secret

# send `fake_hash` and `payload` to server (manually or with sockets)
# REMEMBER: every time you sign new data, you will regenerate a new secret!

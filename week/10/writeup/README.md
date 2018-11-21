Writeup 10 - Crypto II
=====

Name: Jalalah Abdullah
Section: 0101

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Jalalah

## Assignment 10 Writeup

### Part 1 (70 Pts)

# Overview 

I suspected the digital notery living on *nc 142.93.118.186 1234* was susceptible to a [hash length extenion attack](https://en.wikipedia.org/wiki/Length_extension_attack). With that suspicion and having gathered the knowledge the secret was between 6 and 15 bytes, I coded a script to exploit this potential vulnerability. 

To exploit the vulnerability, I made a forged signature (fake_hash) and sent over payload (message + padding + malicious). Now, when the server computes the signature of payload, it will prepend a "secret" which will result in a hash equal to the original fake_hash that was sent in.

This script was programmed using [socket](https://docs.python.org/3/library/socket.html), [struct](https://docs.python.org/2/library/struct.html), and [md5py.py](https://github.com/jalalah/389Rfall18/blob/master/week/10/md5py.py).

# Script Breakdown

I used a socket to connect to the server. I chose option 1 and sent it a message so I could recieve the hash the server outputted. This hash contained my message with a prepended secret attached to it. After I recieved the hash the server sent back, I updated it to have a malicious message attatched to the end of it. This created our fake hash. 

Our fake hash is the first argument we will send to the server when choosing option 2. However, before we send it, we had to craft our payload. Our payload is going to contain our message + padding + malicious (where malicious is the malicious message tacked onto the end of legit). If my suspicion about a hash length extension attack is true, I don't even need to know what the secret is. I could just use the padding.

Deciding what the padding will be is where it got tricky, but luckily I knew the secret message was between 6 and 15 bytes. Thus, I created an loop that tested the different lengths (from 6-15) until I was able to retrieve the flag.

Flag: CMSC389R-{i_still_put_the_M_between_the_DV}

### Part 2 (30 Pts)

Generate your own public key: 

    gpg --gen-key
    
Import someone else's public key: 

    gpg --import pgpassignment.key
    
Encrypt a message for someone else: 

    gpg -e -r "Recipient's Name" message.private
    
Decrypt a message (message.private holds the message meant to encrypt):

    gpg --decrypt message.private.gpg
   
To ensure this worked, I generated my own public/private key, created a text file with a message, then ecrypted and decrypted it.

    gpg --gen-key
    echo "secret message" >> message.private
    gpg -e -r "jalalah" message.private
    gpg --decrypt message.private.gpg
    
After completing these commands, I recieved the encrypted message succesfully. 

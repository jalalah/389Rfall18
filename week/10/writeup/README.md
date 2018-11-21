Writeup 10 - Crypto II
=====

Name: Jalalah Abdullah
Section: 0101

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Jallah

## Assignment 10 Writeup

### Part 1 (70 Pts)

Flag: CMSC389R-{i_still_put_the_M_between_the_DV}

### Part 2 (30 Pts)

Generate your own public key: 

    gpg --gen-key
    
Import someone else's public key: 

    gpg --import pgpassignment.key
    
Encrypt a message for someone else: 

    gpg -e -r "Recipient's Name" message.private
    
Decrypt a message:

    gpg --decrypt message.private.gpg
    
    
where message.private holds the message meant to encrypt

To ensure this worked, I generated my own public/private key, created a text file with a message, then ecrypted and decrypted it.

    gpg --gen-key
    echo "secret message" >> message.private
    gpg -e -r "jalalah" message.private
    gpg --decrypt message.private.gpg
    
After completing these commands, I recieved the encrypted message succesfully. 
    
    



Writeup 9 - Crypto I
=====

Name: Jalalah Abdullah
Section: 0101

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Jalalah Abdullah

## Assignment 9 Writeup

### Part 1 (60 Pts)

# Logistics
To complete this assignment I used the [hashlib](https://docs.python.org/3.5/library/hashlib.html) module in Python.

I knew the recovered hashes were specifically SHA512 password hashes, the passwords came from this password list, and a letter was prepended onto one of these passwords.

With that information I outlined a simple brute force solution of trying each case to crack the passwords.

# Loop Breakdown
I initally started with an outer most loop, this looped through each hash from the [hashes](https://github.com/jalalah/389Rfall18/blob/master/week/9/hashes) file

The loop after that looped through everything in the [wordlist](https://github.com/danielmiessler/SecLists/blob/master/Passwords/probable-v2-top1575.txt)

finally, the innermost loop went through each letter in the alphabet.

Within the innermost loop is where all the computation took place.

# Computation

I prepended everything letter in the alphabet to the current word from the wordlist. 

To perform the SHA512 hash algorithm I used the hashlib.sha512 method.
(Note: password is a salt + a word from teh wordlist concatenated together. 

    encrypt = hashlib.sha512(password)

 After that, I used hexdigest, which returns a string of double length containing only hexadecimal digits, and compared it to the current hash
 
    encrypt.hexdigest() == h.strip('\n')
    
Notice how I am stripping the newline from the end of the hash.

This solution allowed me to uncover the SHA512 password hashes:

* Password1: 
salt: k 
word: neptune

* Password2: 
salt: p 
word: pizza

* Password3: 
salt: u 
word: loveyou

* Password4: 
salt: m 
word: jordan

The complete code can be found [here](https://github.com/jalalah/389Rfall18/blob/master/week/9/writeup/part1.py)
 

### Part 2 (40 Pts)

To complete this assignment I used the [hashlib](https://docs.python.org/3.5/library/hashlib.html) module and [socket](https://docs.python.org/3.5/library/socket.html) library 

I connected the the host 142.93.117.193 through port 7331.

The program had a list of requests to perform certain hashing algorithms on a string of letters and characters. 

I continuously connected to the host using netcat to see the list of hashing algorithms it required:

    nc 142.93.117.193 7331
    
 I uncovered the server only had 6 hashing algorithms it requested.
 
 In my script, I created a socket to recieve and print data from the server. As well as send data to the server. 
 
 I looked for the substring of a hashing algorithm in the data recieved frmo the server. When I matchd with an algorithm, I saved a substring of the data starting from where that hashing algorithm string occured. 
 
 The format of each requeast made it so the fourth word in the substring was the requested string to be hashed.

The output before getting a substring:

    Find me the md5 hash of VXpM25gE55

The output after only saving a substring starting from the requested algorithm:

    md5 hash of VXpM25gE55
    
After finding this pattern, I split the string by spaces and grabbed the string to be hashed by accessing the 3rd index of the array.

    substring = data[index:] # getting the substring starting from the hash algo
  	subarray = substring.split(' ') #splitting the string
  	return subarray[3] # returning what needs to be hashed
    
This was all down in a method that each hash algorithm would call to avoid duplicate code. 

After getting the value to be hashed, I followed a similar pattern to the computation done in part one. 

* Performed the desired hash algorithm using haslib.*desiredAlgorithmHere*(stringToBeHashed)
* Took the value of the last step and used hexdigest on it: returnedValueFromStep1.hexdigit()
* Send that value to the server

This was done 11 times before the flag was uncovered: CMSC389R-{H4sh-5l!ngInG-h@sH3r}






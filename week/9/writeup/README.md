Writeup 9 - Crypto I
=====

Name: Jalalah Abdullah
Section: 0101

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Jalalah Abdullah

## Assignment 9 Writeup

### Part 1 (60 Pts)

# Initial Information

Here is what I knew before completing this assignment:

* The recovered hashes were specifically SHA512 password hashes
* the passwords came from [this](https://github.com/danielmiessler/SecLists/blob/master/Passwords/probable-v2-top1575.txt) wordlist, and were salted by pre-pending a single, lowercase character.

With that information I outlined a simple, brute force solution to crack the SHA512 password hashes. This solution was completed by using the [hashlib](https://docs.python.org/3.5/library/hashlib.html) module in Python.

# Loop Breakdown
I initally started with an outer most loop, this looped through each hash from the [hashes](https://github.com/jalalah/389Rfall18/blob/master/week/9/hashes) file.

The loop after that, or the middle loop, looped through everything in the [wordlist](https://github.com/danielmiessler/SecLists/blob/master/Passwords/probable-v2-top1575.txt), previously mentioned above.

Finally, the innermost loop went through each letter in the alphabet.

Within the innermost loop is where all the computation took place.

# Computation

I prepended everything letter in the alphabet to the current word from the wordlist. 

To perform the SHA512 hash algorithm I used the hashlib.sha512 method and saved the result to a variable.

    encrypt = hashlib.sha512(password)

 After that, I used hexdigest, which returns a string of double length containing only hexadecimal digits, and compared it to the current hash
 
    encrypt.hexdigest() == h.strip('\n') # Must strip the newline from the end of the hash.

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

The complete code can be found [here](https://github.com/jalalah/389Rfall18/blob/master/week/9/writeup/part1.py).


### Part 2 (40 Pts)

# Premise Of The Problem

To complete this assignment I used the [hashlib](https://docs.python.org/3.5/library/hashlib.html) module and [socket](https://docs.python.org/3.5/library/socket.html) library.

I used [netcat](https://en.wikipedia.org/wiki/Netcat) to connect to the host 142.93.117.193 through port 7331. 

    nc 142.93.117.193 7331
    
Once connected to the server, there were a list of requests to perform certain hashing algorithms on a string containing numbers and characters. I continuously connected to the host using netcat to see the list of hashing algorithms it required:
    
 I uncovered the server only had 6 hashing algorithms it requested: SHA512, SHA1, SHA384, SHA224, SHA256, MD5
 
 The hashing requests changed each time you connected to the server, so I created a script that would correctly send the desired hashes to the server no matter the hash algorithm or string to be hashed.
 
 # Script Outline
 
 ### Socket
 
 Within my script, I created a socket to recieve and print data from the server. 
 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("142.93.117.193", 7331))

I also used this socket to send data to the server. 

### Pulling Information From The Server
 
I looked for the substring of a hashing algorithm in the data recieved from the server. This was done just by using a string of if-else if statements. When I matched with an algorithm, I saved a substring of the data starting from where that hashing algorithm string occured. The format of each requeast made it so the fourth word in the obtained substring was the requested string to be hashed.

The output before getting a substring:

    Find me the md5 hash of VXpM25gE55

The output after only saving a substring starting from the requested algorithm:

    md5 hash of VXpM25gE55 # Notice, the fourth string is our desired string to hash
    
After finding this pattern, I split the string by spaces and grabbed the string to be hashed by accessing the 3rd index of the array.

    # index = index where hash algorithm occured
    # data = the string from the server
    substring = data[index:] # getting the substring starting from the desired hash algorithm
  	subarray = substring.split(' ') #splitting the string by spaces
  	return subarray[3] # returning what needs to be hashed
    
This was all completed in a method called *return_password* that each hash algorithm would call to avoid duplicate code. 

After getting the value to be hashed, I followed a similar pattern to the computation done in part one. As an example, say we were using hash algorithm MD5 and the string to be hashed was HG56T3QWK. The steps would be:

1. Perform the desired hash algorithm using hashlib.*desiredAlgorithmHere*(stringToBeHashed) and save the result

        result = hashlib.md5("HG56T3QWK") 

2. Take the value of the last step and use hexdigest on it: returnedValueFromStep1.hexdigit()

        encrypt = result .hexdigest()
        
3. Send that value to the server

        s.send(encrypt)
	s.send("\n")
        
This was done 11 times before the flag was uncovered: CMSC389R-{H4sh-5l!ngInG-h@sH3r}






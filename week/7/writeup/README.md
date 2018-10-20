Writeup 7 - Forensics I
======

Name: Jalalah Abdullah
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Jalalah Abdullah

## Assignment 7 writeup

### Part 1 (40 pts)

1. jpeg file 
 
2. Photo was taken at Michigan Ave, Chicago. The building is named 875 North Michigan Avenue/John Hancock Center
 
3. Date taken: 2018:08:22 11:33:24
 
4. Photo was taken with: IPhone 8 back camera
 
5. 539.5m above Sea Level
 
6. Flags: CMSC389R-{look_I_f0und_a_str1ng} and CMSC389R-{abr@cadabra}

### Part 2 (55 pts)

flag: CMSC389R-{dropping_files_is_fun}

To find the flag I began with simple techniques then moved my way up. 

I used strings and grep to find symbols in the binary. The only useful thing I retrieved from that was a string that said "Where is your flag?". When running the binary, I recieved this same message.

After finding nothing with grep or binwalk, I used a dissembler to look through the binary.

      objdump -d binary
      
From this, I saw multiple methods within the binary, including a main method and another method called reverse array. I also saw at one point a file was being opened, written to, and closed. But I couldn't figure out what that file was or where it was. I poked around some of these methods and didn't find anything useful at first and went through a bunch of useless rabit holes. 

Because the binary produced a string, I decided to find where that string was printed and to look at what was happening in the assembly code before that. 

When doing this, I used radare.

    r2 binary

This allowed me to see strings. After doing this I found a pathway in the comments of the main file

    /tmp/.stego
    
I ran file on this pathway and it returned this information:

    /tmp/.stego: data
    
I used binwalk on this pathway to try and figure out what specific type of data was in this file. 

    binwalk /tmp/.stego: data
    
When running this command, I retrived back information that it was a JPEG file. But if it was a jpeg file why couldn't I open it?

I opened the pathway in Bless, a hex editor, and after looking at the magic bytes, I saw a leading 00 was inserted before the magic bytes of a jpeg file. I removed those extra 0's, saved the image to my computer, and saw that it was a picture of a stegosauras. Still no flag, though!

Luckily, the picture of the stegosauras prompted the idea to use steghide to extract hidden data for it. I ran this command on the image, entered stegosaurus as the passcode, and found the flag. 
    

    

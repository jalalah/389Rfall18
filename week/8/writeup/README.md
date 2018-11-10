Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: Jalalah Abdullah

Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.
Digital acknowledgement of honor pledge: Jalalah Abdullah

 ## Assignment 8 Writeup
 ### Part 1 (45 Pts)

1. the used a traceroute command on the website: cornerstoneairlines.co

2. names used by the hackers: laz0rh4x and c0uchpot4doz

3. hacker's IP addresses: 104.248.224.85 and 142.93.118.186. They're coming from New York

4. port: 2749

5. They're planning to meet on 1500 tomorrow

6. They sent a shared google drive [link](https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing) 

7. Tomorrow

 ### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*

1. The UNIX timestamp was: 1540428007. which is 17829 days after January 1st 1970. Thus, the file was generated on October 25th 2018. 

2. Author: 813326700

3. The file says it has 9 sections, but it really has 11. 

4. All the sections:

First Section: SECTION_ASCI
It had a message:  to call this number to get your flag: (422) 537 - 7946

Second Section: SECTION_WORDS
Had 15 numbers listed: 5 60 3 1 4 1 5 9 2 6 5 3 5 8 9 

Third Section: SECTION_COORD
Had a lattiude, longitide coordinate: (6, 328479099)

Fourth Section: SECTION_REFERENCE
Contained the number 7

Fifth Section: SECTION_ASCI
Had a message: The infmaous security pr0s at CMSC389R will never find this!

Sixth Section: SECTION_ASCI
Had a message about the first recorded uses of steganography 

Seventh Section: SECTION_COORD
Had a lattiude, longitide coordinate: (6, 736452888)

Eighth Section: SECTION_PNG
Not completed yet

Ninth Section: SECTION_ASCI
Had a string of random characters. Can look at it by doing strings update.fpff | grep "saS"

Tenth Section: SECTION_ASCI
Had a string of random characters. Can look at it by doing strings update.fpff | grep "BuL"

Eleventh Section: SECTION_DWORDS
Had six dwords: 2 4 8 15 16 23

5. flags found: 

## Analysis

When beginning to explore this file I was unfamiliar with th structure of it so the spec helped a lot. 
At first, I had a lot of issues figuring out the proper way to unpack all the bytes and went through a lot of trial and error.

I tested different bounds to be sure I was truly getting all the data from within the file. 

For the ASCI generated input, I also did an additional grip on the file with keywords from the code to be sure i pulled out all the text I could from that section.  

Writeup 2 - OSINT (Open Source Intelligence)
======

Name: Jalalah Abdullah
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Jalalah Abdulalh

## Assignment 2 writeup

### Part 1 (45 pts)

1. Fred Krueger

2. Twitter/Instagram/reddit: kruegster1990
Found these accounts by using a username search with inteltechniques
email: kruegster@tutanota.com
I found this in the page source of his website and just googling his username.

3. The IP address: 142.93.118.186. I found this with the tracert linux command. So i did tracert www.cornerstoreairelines.co

4. i found www.cornerstoreairlines.co/secret by using robots.txt, seeing what they didnt allow, and then viewing the page source.
I found this flag CMSC289R-(fly_th3_sk1es_w1th_u5} 

5. the admin page had an IP: 142.93.117.193. 
they linked to a site under construction. they were onin the browser when you clicked on the admin link. they were also in the page source of the website (home and about tabs)

6. The admin page was an associated server. It's on the webpage with a different IP

7. Ubuntu is running on the associated server. I did this by taking the IP address and putting it into shodan

8. <!-- CMSC389R-{fly_th3_sk1es_w1th_u5} -->

### Part 2 (55 pts)

I used inteltechniques to find social media accounts involved with Fred. I found Reddit, Twitter, and Instagram accounts. On his Instagram, there were pictures of a plane ticket. 

I used nmap to find all the ports associated with the admin website IP. I uncovered port 1337 and 10010 were being unused. With nc, I was able to find that port 1337 gave me access to the Cornerstone Airlines administrator portal. 

His username (kruegster) was found on his website. To uncover his password, I used rockyou.txt and looped through them using a python script until I found out what his password was (pokemon)

I went through his home directory, found a directory named flight records, and used the picture of the plane ticket on his instagram to uncover which txt file had the flag in it: CMSC389R -{c0rn3rstone-air-27670}

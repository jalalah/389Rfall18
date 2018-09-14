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

I used inteltechniques to find other social media accounts involved with Fred. On his instagram there were pictures of a plane ticket.
I used nmap to find all the ports associated with the admin website IP. With that, I was able to fain access to the ornerstone Airlines administrator portal. 
I used a lucky guess on his username being either kruegster1990 (what most of his usernames were) or kruegster (what his email is). To uncover his password, I used rockyou.txt

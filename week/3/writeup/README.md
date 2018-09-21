Writeup 3 - OSINT II, OpSec and RE
======

Name: Jalalah Abdullah
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Jalalah Abdullah

## Assignment 3 Writeup

### Part 1 (100 pts)

Fred Kruegster,

Thanks for reaching out to me on how to fix vulnerabilities within your website! I've compiled a list of some actions you can take to give your website, as well as your online accounts in general, better security.

### 1 Open ports

I was able to access the associated server (admin page) of your website through an open port. Open ports are dangerous because they're an attack surface. They can expose information about you and your system that you do not want out there. 

Wikipedia provides a wonderful, yet contaned, description of what open ports are. I highly recommend taking the time to read [this] (https://en.wikipedia.org/wiki/Open_port)!

Pay particular attention to the final three paragraphs, they go over how a port can be closed (which is what you want to do to ports that are unused) by using a firewall. Using a firewall would be a security practice that will prevent security leaks that ports can cause. 

* Firewalls

A firewall can block unauthorized access to your website. Think of it like a security guard and your website is the door this security person is guarding. The security gaurd (firewall) will act as someone who turns away unauthorized visitors to that door (website).

Luckily, there are plenty of guides/tutorials that can help you set up a firewall on your website by yourself! I recommend [this] (https://www.dummies.com/web-design-development/web-hosting/how-to-install-a-firewall-on-your-website/) tutorial. However, there are plenty of other options! Always remember: Google is your friend!

### * Passwords

We all want passwords we can remember. But at the same time, we don't want it to be so easy anyone can come up with the passwords we've chosen. Because of this, you want to avoid choosing passwords that include common phrases, pet names, your favorite sports team, etc.

Let's take your password for example: pokemon

On you Instagram, 99% of what you posted about were Pokemon. Also, on your Twitter you retweeted something pertaining to Pokemon. If I am trying to break into your system, I'm going to start with passwords that are common/what I believe you'd pick. I don't even have to know you personally to think of Pokemon; all I would have to do is look at your social media accounts.

To form a strong password, you want to use more than just lower case characters. Using numbers, capital letters, and symbols all help make your password stronger and more difficult to uncover.

Say you still wanted to choose a password like pokemon. You could definitely do that if you alter the spelling and also make it into a longer phrase using the suggestions I provided above. Here are a few examples (please do not use any of these!):

1. ire11yLOVEp0K3mOn
2. P0K3MON1sMYf@vor!t3
3. p0KEM0N!$0gr34T!

These are phrases that would be easy for you to remember, but they're written in a way that's difficult for people to think up of. They're also phrases that wouldn't be on a basic password list like rockyou.txt (which is the list I used to hack into your system).

For more insentive on choosing a stronger password, take a look at a [hacker's] (http://www.alphr.com/features/371158/top-ten-password-cracking-techniques) perspective when it comes to cracking passwords. Being well informed of what a potential threat will try on you will help you create a password that doesn't match a criteria of an easy breach. 

### Wrap Up

I was able to get as far as I did into your website because of an open port, a weak password, and the personal information (plane ticket) you posted on your instagram (have fun in San Francisco this winter:) ). Even if I got into the port, if you had a really strong password I wouldn't have been able to get any further. If I did so happen to still crack your password, if you hadn't posted your plane ticket online, I wouldn't have been able to know exactly which .txt file pertained to your flight.

We have social media accounts so people can see things we post. But you have to be mindful about what you put out there and the potential danger people can do with your information. Don't make yourself an easy target!

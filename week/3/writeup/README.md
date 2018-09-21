Writeup 3 - OSINT II, OpSec and RE
======

Name: Jalalah Abdullah

Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Jalalah Abdullah

## Assignment 3 Writeup

### Part 1 (100 pts)

Fred Kruegster,

Thanks for reaching out to me on how to fix vulnerabilities within your website! I've compiled a list of some actions you can take to give your website better security.

### Open ports

I was able to access the associated server (admin page) of your website through an open port. Open ports are dangerous because they're an attack surface. They can expose information about you and your system that you do not want out there. 

Wikipedia provides a wonderful, yet contained, description of what open ports are. I highly recommend reading [this](https://en.wikipedia.org/wiki/Open_port)! Pay particular attention to the final three paragraphs, they go over how a port can be closed (which is what you want to do to ports that are unused) by using a firewall. Using a firewall would be a security practice that will prevent security leaks.

* Firewalls

A firewall can block unauthorized access to your website. Think of it like a security guard and your website is the door this security person is guarding. The security gaurd (firewall) will act as someone who turns away unauthorized visitors to that door (website).

Luckily, there are plenty of guides/tutorials that can help you set up a firewall on your website by yourself! I recommend [this](https://www.dummies.com/web-design-development/web-hosting/how-to-install-a-firewall-on-your-website/) tutorial. However, there are plenty of other options! Always remember: Google is your friend!

### Passwords

We all want passwords we can remember. But at the same time, we don't want it to be so easy anyone can come up with the passwords we've chosen. Because of this, you want to avoid choosing passwords that include common phrases, pet names, your favorite sports team, etc.

Let's take your password for example: pokemon

On you Instagram, 99% of what you posted about were Pokemon. Also, on your Twitter you retweeted something pertaining to Pokemon. If I am trying to break into your system, I'm going to start with passwords that are common/what I believe you'd pick. I don't even have to know you personally to think of Pokemon; all I would have to do is look at your social media accounts.

To form a strong password, you want to use more than just lower case characters and a single word. Using numbers, capital letters, and symbols will all help make your password stronger and more difficult to uncover.

Say you still wanted to choose a password involving pokemon. You could definitely do that if you alter the spelling and also make it into a longer phrase using the suggestions I provided above. Here are a few examples (please do not use any of these!):

1. ire11yLOVEp0K3mOn
2. P0K3MON1sMYf@vor!t3
3. p0KEM0N!$0gr34T!

These are phrases that would be easy for you to remember, but they're written in a way that's difficult for people to think up of. They're also phrases that wouldn't be on a basic password list like [rockyou.txt](https://www.scrapmaker.com/view/dictionaries/rockyou.txt) (which is the wordlist I used to hack into your system).

For more incentive on choosing a stronger password, take a look at a [hacker's](http://www.alphr.com/features/371158/top-ten-password-cracking-techniques) perspective when it comes to cracking passwords. Being well informed of what a a hacker's tactics are will help you defend yourself better. 

Some final notes: 
1. Don't use the same password across different accounts
2. Write your passwords down on *paper* (as opposed to keeping it in a document on your laptop or in notes on your phone)
3. Don't share your passwords with anyone! And if you *do* have to share your password with someone, for whatever reason, don't share it through the internet! (e.g. an email or text)

### Social Media Safety

From your Twitter alone I was able to find out where you lived, your Instagram account, your Reddit account, your email, and your company website. I didn't do anything beyond using google (and other techniques mentioned in my publushed report) to search for this information. 

Now, knowing all this information through the internet isn't necessarily bad. Social media was created as an outlet to get to know people and stay connected. In fact, most social media accounts give an option to put a location, birthday, personal links (like your website), etc. Yet, knowing that all this information is out there for anyone and everyone to see, you have to be mindful of what you post. 

The plane ticket that you posted on your Instagram might've seemed like an innocent post, but not everyone will look at that and think 'oh nice, he's going to San Francisco!'. Some people can take that information to harm you. In my case, that information was used to find which flight record pertained to you (after I broke into your admin page through an open port and weak password). 

There are practices to make your social media accounts more secure. Some examples are making your account private, only letting people you know follow you, and a strong password. For further practices, [Investor.gov](investor.gov), a website dedicated to fight against fruad, has provided a short [article](https://www.investor.gov/protect-your-investments/fraud/how-avoid-fraud/protect-your-social-media-accounts) on how to protect your online accounts.

We have social media accounts so people can see things we post. However, you have to be mindful about what you put out there and the potential danger people can do with your information. Don't make yourself an easy target!

### Wrap Up

I was able to get as far as I did into your website because of an open port, a weak password, and the personal information (plane ticket) you posted on your instagram. Even if I discovered the open port, if you had a really strong password I wouldn't have been able to get any further. If I did so happen to still crack your password, if you hadn't posted your plane ticket online, I wouldn't have been able to know exactly which .txt file pertained to your flight.

There is no way to have perfect security online, but we want to get as close to perfection as possible. By building solid security walls, one behind another, you can save yourself from getting breached. 

If you have any further questions about something I've listed here, or any other inquiries pertaining to security, please reach out to me again! 

All the best,

Jalalah



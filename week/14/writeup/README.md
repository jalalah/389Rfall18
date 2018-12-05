Writeup 10 - Crypto II
=====

Name: Jalalah Abdullah
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Jalalah

## Assignment 10 Writeup

### Part 1 (70 Pts)


### Part 2 (30 Pts)

#Level 1: 

From slide 70 of [this](https://www.cs.umd.edu/class/fall2018/cmsc330/lectures/22-web-security.pdf) slideset (specifically slide 70), I got the command:

    <script>alert(0)</script> 
when executed into the first challenge, it succeeded. 

#Level 2:

I tried the same command from level 1, however, my message didn't even pop up. I proceeded to try different ways to write out javascript tags (make spaces and new lines between characters), however, they still would not execute or even show up on the message board. 

From the same slide set mentioned previously, I got the idea to execute Javascript through CSS instead by using a background image URL: 

    <div style="background-image:url(javascript:alert(’JavaScript’))"></div>
    
However, this does not work. I then searched if I could execute JavaScript through an HTML tag. I found [this](https://stackoverflow.com/questions/37435077/execute-javascript-for-xss-without-script-tags) useful post which showed me how to execute an alert hidden within HTML.

    <img src=0 onerror=alert(1)>
    
With this, I passed level 2.

#Level 3: 

Initially, I began tagging on script commands to the end of the URL just to see what happened. This didn't get me anywhere. I decided to inspect each image and I foumd that what I typed into the search bar was concatenated within an HTML img tag. I continuously tried to execute the script "=0 onerror = alert(0)" but nothing happenned. I tried to add semi colons before and after, I tried closing the image url and creating a new one with my malicious attack, I tried executing my malicious code and commenting out whatever went after that.

After much back and forth, I eventually toggled the code and view index.html. It was there that I realized single quotes were being used in the img tag. I swapped my initial double quote out for that and my alert went through.  

    ' onerror = "alert(0)";

#Level 4:

I toggled the code and viewed all the hints before I even had an idea how to start approaching this level. 

When I inserted the single ' into the timer input, I viewed the error console and saw this: 

        SyntaxError: '' string literal contains an unescaped line break
        
I kept playing around with the URL and viewing the error console, but I keptgoing further and further down a rabbit hole that lead nowhere.

After seeking some assistance, I realized this line in timer.html:

        <img src="/static/loading.gif" onload="startTimer('{{ timer }}');" />
   
From the set up, it was possible to escape it so that the onload="startTimer('..." escapes early.

Initally, I tried

        https://xss-game.appspot.com/level4/frame?timer=');alert(0);

But that did not execute, it was then I realized there was a lingering ') within the code that I had to close, so there was no syntax error. 

        https://xss-game.appspot.com/level4/frame?timer=');alert(0);('

However, this still did not work. After reviewing the hints, I was reminded of how when browsers parse tag attributes, the HTML decode their values. I used [this]() site to encode everything from the previous attempt except 'alert(0)'

       https://xss-game.appspot.com/level4/frame?timer=%27%29%3Balert(0)%3B%28%27
 
This succeeded and I passed to the next round!

#Level 5:

This level I passed within my first few dummy tries in launching an attack.

My first try I was putting <script>alert(0)</script> into the URL and executing that. That did not work. Then, I tried doing javascript:alert(0) and it worked!!

So the steps I took

* https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert(0); 
* entered in anything into the mail bar
* submit next

All done
 
#Level 6:



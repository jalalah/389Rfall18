Writeup 3 - Pentesting I
======

Name: Jalalah Abdullah
Section: 0101

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Jalalah Abdullah

## Assignment 4 Writeup

### Part 1 (45 pts)

Upon hearing rumors of Cornerstone Airline's new server being vulnerable to a [command injection attack](https://www.netsparker.com/blog/web-security/command-injection-vulnerability/), I tested for the vulnerability myself. 

Using netcat for banner grabbing, I entered into the server with the command: 

*nc cornerstoreairlines.co 45*. 

Afterwards, I was prompted to enter an IP Address.

When entering the desired data, the execution went as expected: I recieved data back on the reachability of the host. This is what Fred Krueger's intention was: To remotely be able to check availability of internet connected device's on his company's network.

However, by just tacking extra commands onto the input, like this: 

*8.8.8.8; ls*

I was able to get into the root of Fred's server and execute my own commands. Thus, his server is vulenerable to a command injection attack!


With further more exploring, I found the shell Krueger is using to check uptime. The shell was located in the opt directory. In Krueger's shell, he's accepted everything the user type into the command line as input. This is why you're able to execute commands beyond what Krueger's intended input.

To fix this issue, Krueger can use input validation to ensure the only thing the command accepts is a proplery formatted IP Adress and nothing else. 

The flag that was found in the home directory: CMSC389R-{p1ug_as_a_$erv1c3}

Once in your server, I was prompted to enter an IP Address. 

### Part 2 (55 pts)

In order to execute multiple commands, I'd have to execute them all together as one input with semi colons separated individual commands. This is the input I entered to find the flag: 

*garbage; cd home; cat flag.txt*

The reason everything has to be within a single string is because the server kicks you out after receiving just a single input string.

I leveraged this vulnerability by creating a Python script that allowed an interactive shell. With this script, you'll be able to navigate through Krueger's server as you would on any other command line. 

The script includes 4 options (the commands are in parenthesis):

* To launch into an interactive shell (shell)
* Display a help menu (help)
* Download files (pull <remote path> <local path>)
* Quit (quit)

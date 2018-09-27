Writeup 3 - Pentesting I
======

Name: Jalalah Abdullah

Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Jalalah Abdullah

## Assignment 4 Writeup

# Exploiting Cornerstone Airline's Vulnerability 

Upon hearing rumors of Cornerstone Airline's new server being vulnerable to a [command injection attack](https://www.netsparker.com/blog/web-security/command-injection-vulnerability/), I tested for the vulnerability myself. A Command Injection attack is when a user (or application) is able to pass data to a system by tagging the data onto an already antincipated response. For example, if a system is expecting a username, you can provide the username and then add extra data after. With the additional data,the system will receive and execute it if it's vulnerable to a Command Injection attack. Knowing about the rumors and the format of Command Injection attacks, I entered into Fred Kreuger's newly created server with a goal to exploit this potential vulnerability. 

Using netcat to connect to Cornerstone Airline's system, I entered the command: 

*nc cornerstoreairlines.co 45* 

Once remotely connected to the system, I was prompted to enter an IP address.

When I entered an IP address, the execution went as expected and I recieved data back involving the reachability of the host. This is what Krueger's intention was with this new server: to remotely be able to check uptime of internet connected device's on his company's network.

However, by just tacking extra commands onto the input, like this: 

*8.8.8.8; ls*

I was able to execute commands on the root of Krueger's server. In fact, I could enter anything as my first command and still gain access. It didn't even have to be a valid IP address!

*garbage; ls*

Now, it's obvious Kreuger's new shell is vulnerable to a Command Injection attack. I set out to find out what was allowing extra commands to be executed.

With further exploring, I uncovered the shell Krueger is using to check uptime. The shell, named *container_startup.sh*, was located in the opt directory. In Krueger's shell, he's accepting *everything* the user types into the command line as input. This is why the server allows you to execute commands beyond what Krueger intended to be executed.

To fix this issue, Krueger can use input validation to ensure the only string that is accepted is a properly formatted IP Adress and nothing else. 

The flag that was found in the home directory: CMSC389R-{p1ug_as_a_$erv1c3}

# Creating An Interactive Shell

In order to execute multiple commands on Cornerstone Airline's server, I'd have to input them all together as one string with semicolons separating the individual commands. As an example, this is the input I entered to find the flag: 

*garbage; cd home; cat flag.txt*

The reason everything has to be within one string is because the server kicks you out after receiving a single input (that is how Krueger constructed his shell).

I leveraged this vulnerability by creating a Python script.

## Layout Of The Script

The script is structured with two shells: an outer shell and inner shell. 

The only commands you can execute on the outer shell are as follows:

* To launch into the interactive (inner) shell: shell 
* Display a help menu: help
* Download files: pull <remote path> <local path>
* Quit: quit

The inner shell (what's launched when executing shell) allows you to be directly on the Cornerstone Airline's server. With this, you'll be able to navigate through Krueger's server with full root privilidges. 

## Makeup Of the Script

The script was created in a simple manner, it only requires: a single method, loops, conditionals, and a socket. 

When first running the code, you are within the outer shell and are restricted to the four commands listed above. Each command eligible within the outer shell are executed by using if statements then calling the desired *execute_cmd* method. 

When launching the inner shell, a similiar process takes place. The only difference is tracking the directory the user cd's into. 

The shell code can be found [here](https://github.com/jalalah/389Rfall18/blob/master/week/4/shell.py). 

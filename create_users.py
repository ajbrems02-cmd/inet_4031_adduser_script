#!/usr/bin/python3

# INET4031
# AJ Bremer
# 10/30/2025
# 10/30/2025

#os - give python the ability to run os commands
#re - givespython the ability to manipulate text patterns
#sys - gives python access to system specific file i/o operations, like the sys.stdin command used below
import os
import re
import sys

def main():
    for line in sys.stdin:

        #The match variable is being used to find a line in the input file beginning with the '#' character and
	#then skipping over it.
        match = re.match("^#",line)

        #This line is splitting the lines of the input file by the ':' character
        fields = line.strip().split(':')

        #appropriate comment: checks validity of input line
        #if the if statement is true, then the continue block will be triggered and skip the line of input
        #the if statement evaluates the match and fields variables, pretty much if the line contains a # character
	#or fields is not equal to 5, then the continue function is triggered and the line is skipped
        if match or len(fields) != 5:
            continue

        #These lines are used to break apart the input that was assigned to the fields variable above into different chunks
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #This is being done in the event that a user is being added to multiple groups, such as user06 in the input file
        groups = fields[4].split(',')

        #print statement shows progress on terminal for users
        print("==> Creating account for %s..." % (username))
        #The cmd variable here contains a string which is formatted as a command line prompt
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #print cmd
        os.system(cmd)

        #progress statement, if a bug appears it could potentially get caught here
        print("==> Setting the password for %s..." % (username))
        #I believe this line is assigning the password in the passwd directory for the user the program is currently on.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #os command gives the program special privileges to interact with the operating system
        os.system(cmd)

        for group in groups:
            #if the group variable is equal to the '-' character, that line of input has no assigned group and the loop is skipped
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()

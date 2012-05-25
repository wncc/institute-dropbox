global username,password
import getpass
print "Enter your LDAP id and Password \n"
username= raw_input('Username : ')
password= getpass.getpass('Password : ')

from ftplib import FTP
global ftp
ftp = FTP ('home.iitb.ac.in')
ftp.login(username,password)
print "Welcome "+ username + " to your bighome home folder."


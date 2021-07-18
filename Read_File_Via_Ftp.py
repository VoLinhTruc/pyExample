#Aplication content: Get data in cc.txt from ftp server 192.168.1.50 and print to console

import ftplib
from time import sleep

ftp_read_str = "12"

def handle_binary(data):
	global ftp_read_str
	ftp_read_str = data

ftp = ftplib.FTP('192.168.1.50')
ftp.login()

while(1):
	ftp.retrbinary("RETR cc.txt", handle_binary)
	# print ftp.sendcmd("RETR cc.txt")
	print(ftp_read_str)
	sleep(0.1)
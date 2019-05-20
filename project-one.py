#!/usr/bin/env python3

import socket

#create an INET, raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

domain = 'www.anbetechsolutions.com'

# get ip address
ip = socket.gethostbyname(domain)

print ('IP address')
print(ip)

#get fully qualified domain name

domainname = socket.getfqdn(domain)

print ('Fully qualified domain name')

print(domainname)

print ('Data from socket for TCP protocol')

# receive a packet
while True:
  print (s.recvfrom(65565))
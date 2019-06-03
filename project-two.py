#!/usr/bin/env python3

import socket
import struct

def main():

    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    domain = 'www.anbetechsolutions.com'

    # get ip address
    ip = socket.gethostbyname(domain)

    print ('IP address')
    print (ip)

    #get fully qualified domain name

    domainname = socket.getfqdn(domain)

    print ('Fully qualified domain name')

    print (domainname)

    print ('Data from socket for TCP protocol')

    while True:
        print(s.recvfrom(65536))
        raw_data, addr = s.recvfrom(65536)
        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
        print('\nEthernet Frame:')
        print('Destination Address: {}, Source Address: {}, Protocol: {}'.format(dest_mac, src_mac, eth_proto))


def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]

def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()

main()


#!/usr/bin/env python3

from urllib.request import urlopen

def get_wan_ip():
    '''
    get the wan ip of current pc.
    '''
    my_ip = urlopen("http://ip.42.pl/raw")
    return my_ip.read()


if __name__ == "__main__":
    ip = get_wan_ip()
    print(ip)
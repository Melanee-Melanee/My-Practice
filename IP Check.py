
# from requests import get
# ip = get('https://checkip.amazonaws.com').content.decode('utf8')
# print('My public IP address is: {}'.format(ip))  
#     # https://api.ipify.org
    # https://checkip.amazonaws.com
    # https://icanhazip.com
    # https://ifconfig.co/ip
    # https://ipecho.net/plain
    # https://ipinfo.io/ip
#nslookup in linux can find an IP for a custom website

#-------------------------------------------------------------------

# import public_ip as ip
# print(ip.get())

#---------------------------------------------------------------------------

#turn on vpn
# import requests
# import json
# def get():
#     endpoint = 'https://ipinfo.io/json'
#     response = requests.get(endpoint, verify = True)
#     if response.status_code != 200:
#         return 'Status:', response.status_code, 'Problem with the request. Exiting.'
#         exit()
#     data = response.json()
#     return data['ip']
# #get my ip
# my_ip = get()

# #print my ip
# print(my_ip)

#----------------------------------------------------------------------------
# Python Program to Get  local IP Address
# import socket
# hostname = socket.gethostname()
# IPAddr = socket.gethostbyname(hostname)

# print("Your Computer Name is:" + hostname)
# print("Your Computer IP Address is:" + IPAddr)


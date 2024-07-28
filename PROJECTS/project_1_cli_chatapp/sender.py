import socket
s =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# target_ip ="192.168.239.249"
target_ip ="127.0.0.1"  #for single person
port_no = 2525
target_address =(target_ip,port_no)

condition= True
while condition:
# while True: both are same
    message =input('plz write your message here :')
    encrypt_message = message.encode("ascii")
    s.sendto(encrypt_message,target_address)

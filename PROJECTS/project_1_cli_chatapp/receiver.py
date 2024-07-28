import socket
import time
t=time.time(time.localtime,time.get_clock_info)

s =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# ip_address="192.168.239.224"
ip_address="127.0.0.1" #for single person
port_no=2525 #range of port no 0-65353 from which some are reserved
complete_address=(ip_address,port_no)
s.bind(complete_address) #s.bind take exactly one value
 
print("hey i am recieving your messages")
while True:
    message=s.recvfrom(100)
    print(message)#(b'lucknow',('127.0.0.1',58763))
    sender_address =message[1][0]#127.0.0.1 it will only give ip if we use 0
    recieved_messagee = message[0]
    

    decrypted_message = recieved_messagee.decode('ascii')
    print(decrypted_message)
    # s.sendto()
    with open(sender_address+'.txt','a+') as file:
        file.write(decrypted_message +'\n')
        #add time and date in txt file
        # recieved_message
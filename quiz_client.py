import socket
from threading import Thread

# asking user to choose a nickname
nickname = input("Enter your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# defining ip address and port number on which the server will run
ip_address = '127.0.0.1'
port = 8000

# connect client to server
client.connect((ip_address, port))

# function to receive the messages sent from server
def receive():
    while True:
        try:
            message = client.recv(2048).decode('utf-8') # decoding the encrypted message
            
            # checking if the received message is NICKNAME
            if message == 'NICKNAME':
                # sending server the user's nickname
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Error occured")
            client.close() # closing client socket
            break

# function to receive message from user that needs to be sent to server
def write():
    while True:
        message = '{}:{}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))

receive_thread = Thread(target=receive)
receive_thread.start()

write_thread = Thread(target=write)
write_thread.start()
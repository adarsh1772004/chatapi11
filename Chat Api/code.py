import socket
from threading import Thread
nickName = input("enter your nick name")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipaddress = '127.0.0.1'
port = 8000
client.connect((ipaddress, port))
print('connected with the surver')


def recive():
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message == 'NICKNAME':
                client.send(nickName.encode('utf-8'))
            else:
                print(message)
        except:
            print('an error ocuerd')
            client.close()
            break


g = GUI()


def goahead(self, name):
    self.login.destroy()
    self.name = name
    rcv = Thread(target=self.recive)
    rcv.start()


def write(self):
    self.textCons.config(state=DISABLED)
    while True:
        message = (f'{self.name}:{self.msg}')
        clint.send(message.encode('utf-8'))
        self.show_message(message)
        break


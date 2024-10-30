import socket
from faker import Faker
import threading
import time
faker = Faker()

def t():
    while True:
        host = faker.ipv4()
        port = 80

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(5)
        try:
            client.connect((host,port))
    
            client.send(b"GET / HTTP/1.1\n\r\nUser-Agent: Love\n\r\n")
          
            response = client.recv(2048).decode()
            f = open("websites/" + host, "w")
            f.write(response)
            while len(response) > 0:
                r = client.recv(2048)
                f.write(r.decode())
                f.flush()
                response += r.decode()
                print(r.decode())
       
        except Exception as e:
        	print(e)
for i in range(0, 16):
    th = threading.Thread(target=t)
    th.start()
    time.sleep(0.25)

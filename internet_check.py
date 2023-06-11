import socket, time, datetime


def check_connectivity():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    online = True
    try:
        PORT = 443
        HOST = socket.gethostbyname("www.google.com")

        connect = s.connect_ex((HOST, PORT))
        
        if connect != 0:
            raise Exception
        
    except Exception as error:
        online = False
        print(error)

    s.close()
    return online

while True:
    log = open("log.txt", "a")

    now = datetime.datetime.now()
    text = f"[{now.day}-{now.month}-{now.year} {now.hour}:{now.minute}:{now.second}] internet connection: {check_connectivity()}\n"

    print(text)
    log.write(text)
    time.sleep(2)
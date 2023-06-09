import socket, time, datetime

def check_connectivity():
    online = True
    try:
        socket.gethostbyname("www.google.com")
    except:
        online = False

    return online

while True:
    log = open("log.txt", "a")

    now = datetime.datetime.now()
    log.write(f"[{now.day}-{now.month}-{now.year} {now.hour}:{now.minute}:{now.second}] internet connection: {check_connectivity()}\n")
    time.sleep(60)
from socket import *
from datetime import datetime
from threading import Thread
import wmi


def dt():
    curr_dt = datetime.now()
    return curr_dt


def pagefile_size():
    comp = wmi.WMI()
    for i in comp.Win32_PageFileUsage():
        res = i.AllocatedBaseSize * pow(2, 20)
        return res


def pagefile_avail():
    comp = wmi.WMI()
    for i in comp.Win32_PageFileUsage():
        avail = (i.AllocatedBaseSize - i.CurrentUsage) * pow(2,20)
        return avail


def handle_client(user, addr):
    while True:
        user.send(f"{dt()} Decide what you want to do: get pagefile size, pagefile's available bytes or nothing\n"
                  "Type pagefile or free or no".encode('utf-8'))
        msg = user.recv(1024).decode('utf-8')
        print(f'CLIENT MSG: {msg}')

        if msg == 'no':
            print(f'{dt()} Goodbye... {addr}\n')
            break
        elif msg == 'pagefile':
            res = pagefile_size()
            print(f'{dt()}\nPagefile size: {res} bytes\n')
        elif msg == 'free':
            avail = pagefile_avail()
            print(f'{dt()}\nPagefile has {avail} available bytes\n')
        else:
            print(f'{dt()} Incorrect query!\n')


def main():
    try:
        server = socket(AF_INET, SOCK_STREAM)
        ip = '192.168.1.102'
        port = 5678
        server.bind((ip, port))
        server.listen()
        print(f'\n{dt()} Waiting for connection...\n')

        while True:
            user, addr = server.accept()
            print(f'{dt()} Successful connection to server2!\n')
            thread = Thread()
            thread.start()
            handle_client(user, addr)
            thread.join()

    except OSError:
        print('Something went wrong...')
    finally:
        server.close()


if __name__ == "__main__":
    main()

from socket import *
from threading import Thread
from datetime import datetime
from win32gui import FindWindow, GetClientRect, GetWindowText, SetWindowText


def dt():
    curr_dt = datetime.now()
    return curr_dt


def frame_size(msg_name):
    window_name = msg_name
    hwnd = FindWindow(None, window_name)

    rect = GetClientRect(hwnd)
    width = rect[2] - rect[0]
    height = rect[3] - rect[1]

    return width, height


def change_name(msg_name, msg_new_name):
    hwnd = FindWindow(None, msg_name)
    SetWindowText(hwnd, msg_new_name)

    hwnd = FindWindow(None, msg_new_name)
    new_name = GetWindowText(hwnd)

    return msg_name, new_name


def handle_client(user, addr):
    while True:
        user.send(f"{dt()}\nDecide what you want to do: get frame size, change server's name or nothing\n"
                  "Type frame or name or no".encode('utf-8'))
        msg = user.recv(1024).decode('utf-8')
        print(f'CLIENT MSG: {msg}')

        if msg == 'no':
            print(f'{dt()} Goodbye... {addr}\n')
            break

        if msg == 'frame':
            user.send(f"{dt()}\nIs server's current name: C:\Windows\system32\cmd.exe - server1.py\n"
                      f"Type y/n".encode('utf-8'))
            msg_ans = user.recv(1024).decode('utf-8')

            if msg_ans == 'n':
                user.send(f"{dt()}\nType server's current name: ".encode('utf-8'))
                msg_name = user.recv(1024).decode('utf-8')
                width, height = frame_size(msg_name)

            else:
                msg_name = 'C:\Windows\system32\cmd.exe - server1.py'
                width, height = frame_size(msg_name)
            print(f'{dt()}\nFrame width: {width}\nFrame height: {height}\n')

        elif msg == 'name':
            user.send(f"{dt()}\nIs servers' current name: C:\Windows\system32\cmd.exe - server1.py \n"
                      f"Type y/n".encode('utf-8'))
            msg_ans = user.recv(1024).decode('utf-8')

            if msg_ans == 'n':
                user.send(f"{dt()}\nType server's current name: ".encode('utf-8'))
                msg_name = user.recv(1024).decode('utf-8')
                user.send(f'{dt()}\nType new name: '.encode('utf-8'))
                msg_new_name = user.recv(1024).decode('utf-8')
                name, new_name = change_name(msg_name, msg_new_name)

            else:
                msg_name = 'C:\Windows\system32\cmd.exe - server1.py'
                user.send(f'{dt()}\nType new name: '.encode('utf-8'))
                msg_new_name = user.recv(1024).decode('utf-8')
                name, new_name = change_name(msg_name, msg_new_name)
            print(f'{dt()}\nCurrent window name: {name}\nNew window name: {new_name}\n')

        else:
            print(f'{dt()} Incorrect query!\n')


def main():
    try:
        server = socket(AF_INET, SOCK_STREAM)
        ip = '192.168.1.102'
        port = 1234
        server.bind((ip, port))
        server.listen()
        print(f'\n{dt()} Waiting for connection...\n')

        while True:
            user, addr = server.accept()
            print(f'{dt()} {addr} Successful connection to server1!\n')
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
